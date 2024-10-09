from django import forms
from .models import Comment, RoomPost


class RoomPostForm(forms.ModelForm):
    """
    Create post form
    """
    class Meta:
        model = RoomPost
        fields = ['title', 'post_user', 'featured_image', 'description', 'available_from', 'available_to']
        widgets = {
            'available_from': forms.DateInput(attrs={'type': 'date'}),
            'available_to': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)