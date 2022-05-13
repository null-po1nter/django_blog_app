from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 
            'content',
            'category',
            'tags',
            'is_published'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            'category': forms.Select(attrs={'class': 'form-control', 'empty_label': None}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'empty_label': None})
        }
