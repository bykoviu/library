from .models import Comment
from django.forms import ModelForm, TextInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'comm']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'comm': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add your comment'
            })
        }