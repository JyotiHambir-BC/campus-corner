from django.contrib import admin
from .models import RoomPost,Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(RoomPost)

class RoomPostAdmin(SummernoteModelAdmin):

    list_display = ('title','created_on','updated_on','available_from','available_to','approved_on')
    summernote_fields = ('description',)

admin.site.register(Comment)