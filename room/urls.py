from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_view, name='home'),
    path('browse/', views.PostList.as_view(), name='browse_rental'),    
    path('post_details/<int:post_id>/',views.post_detail, name='post_details'),
    path('post_details/<int:post_id>/edit_comment/<int:comment_id>',views.comment_edit, name='comment_edit'),
    path('post_details/<int:post_id>/delete_comment/<int:comment_id>/',views.comment_delete, name='comment_delete'),
    path('post_room/', views.post_room, name='post_room'),
    
]