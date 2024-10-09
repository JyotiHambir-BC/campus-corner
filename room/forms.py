from django import forms
from .models import Comment, RoomPost


class RoomPostForm(forms.ModelForm):
    """
    Create post form
    """
    class Meta:
        model = RoomPost
        fields = ['title', 'post_user', 'featured_image', 'description', 'availiable_from', 'availiable_to']
        widgets = {
            'availiable_from': forms.DateInput(attrs={'type': 'date'}),
            'availiable_to': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)