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

    def __init__(self, *args, **kwargs):
        """Set the form styling class
        """

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-input'
