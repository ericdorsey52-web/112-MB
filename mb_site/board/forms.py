from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'required': True}),
            'body': forms.Textarea(attrs={'required': True, 'rows': 4}),
        }
