from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_view, name='home'),
    path('browse/', views.PostList.as_view(), name='browse_rental'),
    path('post_room/', views.post_room, name='post_room'),
    # path('<>/',views.post_detail, name='post_detail'),
    # path('<>/edit_comment/<int:comment_id>',views.comment_edit, name='comment_edit'),
    # path('<>/delete_comment/<int:comment_id>',views.comment_delete, name='comment_delete'),
]