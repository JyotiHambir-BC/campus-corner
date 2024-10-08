from django.contrib import admin
from .models import RoomPost,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(RoomPost)

class RoomPostAdmin(SummernoteModelAdmin):

    list_display = ('title','created_on')
    summernote_fields = ('description',)
