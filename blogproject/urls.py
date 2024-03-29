from django.contrib import admin
from django.urls import path, include
from blogapp import views

from rest_framework import routers


from django.contrib import admin
from django.urls import path
from users.views import * 
from blogapp.views import *
from blogapp.views import PostModelViewSet

router = routers.DefaultRouter()
router.register('blogapp', PostModelViewSet)

urlpatterns = [
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('new/', views.new, name = 'new'),
    path('community/', views.community, name = 'community'),
    path('mbtitest/', views.mbtitest, name = 'mbtitest'),
    path('detail/<int:post_id>', views.detail, name = 'detail'),
    path('edit/<int:post_id>', views.edit, name = 'edit'),
    path('delete/<int:post_id>', views.delete, name = 'delete'),
    path('edit_comment/<int:comment_id>', views.edit_comment, name = 'edit_comment'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name = 'delete_comment'),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('', include(router.urls)),
    path('category_post_create/', category_post_create.as_view()),
    path('category_post_lookup/', category_post_lookup.as_view()),
    path('myposts_lookup/', myposts_lookup.as_view()),
    path('mycomments_lookup/', mycomments_lookup.as_view()),
    path('userposts_lookup/', userposts_lookup.as_view()),
    path('postslike/', postslike.as_view()),


]
