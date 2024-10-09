from django import forms
from .models import Comment, PostList


class RoomPostForm(forms.ModelForm):
    """
    Create post form
    """

    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)