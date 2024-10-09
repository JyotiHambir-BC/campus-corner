from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class RoomPost(models.Model):
    """
        model for room post
    """
    title = models.CharField(unique=True)
    
    post_user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "room"
    )
    featured_image = CloudinaryField('image',default ='placeholder')
    description = models.TextField(null = True)
    updated_on = models.DateTimeField(auto_now =True)
    created_on = models.DateTimeField(auto_now=True)
    available_from = models.DateField()
    available_to = models.DateField()
    approved_on = models.BooleanField(default=False)

    # to do add method to change the dateField of availible to and from 

    def __str__(self):
        return f"The title of the post is {self.title}"

    class Meta:
        ordering = ["created_on",]
    
    def __str__(self):
        return f"{self.title}|post by {self.post_user}"

class Comment(models.Model):
    """
        model for room post's comments
    """
    post = models.ForeignKey(
        RoomPost,
        on_delete = models.CASCADE,
        related_name = "comments"
    )

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "commenter"
    )
    class Meta:
        ordering = ["-created_on",]

    def __str__(self):
        return f"Comment{self.user}"

    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True) 