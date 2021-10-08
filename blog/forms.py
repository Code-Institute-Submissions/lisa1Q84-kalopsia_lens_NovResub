from django import forms
from .models import BlogPost


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        exclude = ('date',)
        fields = ('title', 'article')

    article = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'cols': 20}
        )
    )
