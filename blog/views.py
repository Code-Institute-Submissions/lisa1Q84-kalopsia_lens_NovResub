from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogForm

# Create your views here.


def view_blog(request):
    """ View blog page and superusers can post blog posts.
    """

    # Submit Post
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        # Save Post if form is valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrats, your Post was published!')

        # Send error maessage if the form is invalid
        else:
            messages.error(
                request,
                'Post failed to be published. Please check your form inputs.'
            )
    else:
        form = BlogForm()

    # Order posts by date by default

    posts = BlogPost.objects.all().order_by('-date')

    context = {
        'form': form,
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


@login_required
def edit_post(request, post_id):
    """ (SUPER USERS ONLY)
    Edit a blog post
    """

    # Only allows superusers (Site Admins) to view this page.
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied. Site Admins Only')
        return redirect(reverse('home'))

    # Get Post
    post = get_object_or_404(BlogPost, pk=post_id)

    # Handles Form submission
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)

        # Save Product if form is valid and redurect back to product management
        if form.is_valid():
            post.title = form.cleaned_data.get('title')
            post.article = form.cleaned_data.get('article')
            post.date = request.POST.get('date')
            post.save()
            messages.success(request, 'Post Updated')
            return redirect(reverse('blog'))

        # Send error maessage if form invalid
        else:
            messages.error(
                request,
                'Updating post failed. Please check your form inputs.'
            )
    else:
        form = BlogForm(instance=post)
        messages.info(request, f'Warning you are editing {post.title}')

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'blog/edit_post.html', context)


@login_required
def delete_post(request, post_id):
    """ (SUPER USERS ONLY)
    Delete a Blog from the site
    """

    # Only allows superusers (Site Admins) to view this page.
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied. Site Admins Only')
        return redirect(reverse('home'))

    # Get object
    post = get_object_or_404(BlogPost, pk=post_id)

    # Delete object
    post.delete()

    current_page = request.POST.get('current_page')

    # Give user feedback and redirect
    messages.success(request, 'Post deleted')
    return redirect(current_page)
