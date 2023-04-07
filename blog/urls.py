from django.urls import path

from blog.views import index, archive, post_detail, tag, register, post_page, post_create, comment_create, my_posts, \
    tornar_staff, staff_page, tag_page, tag_create, post_edit, post_update, post_delete

urlpatterns = [
    path('', index, name='index'),

    path('register/', register, name='register'),

    path('post_page/', post_page, name='post_page'),
    path('post_create/', post_create, name='post_create'),
    path('post_edit/<int:id>/', post_edit, name='post_edit'),
    path('post_update/<int:id>/', post_update, name='post_update'),
    path('post_delete/<int:id>/', post_delete, name='post_delete'),
    path('post_detail/<int:id>/', post_detail, name='post_detail'),
    path('my_posts/<int:user_id>/', my_posts, name='my_posts'),

    path('comment_create/<int:id>/', comment_create, name='comment_create'),

    path('tag/<str:tag>/', tag, name='tag'),
    path('archive/<str:data>/', archive, name='archive'),

    path('staff_page/', staff_page, name='staff_page'),
    path('tornar_staff/', tornar_staff, name='tornar_staff'),

    path('tag_page/', tag_page, name='tag_page'),
    path('tag_create/', tag_create, name='tag_create'),
]
