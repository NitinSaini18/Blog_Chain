from django.urls import path
from . import views
app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name = "blog_list"),    
    path('write/', views.CreateBlog.as_view(), name = "blog/create_blog/"),    
    path('blog_details/<str:slug>/', views.blog_detail, name = "blog_detail"), 
    path('liked/<pk>/', views.liked, name = "liked_post"),    
    path('unliked/<pk>/', views.unliked, name = "unliked_post"), 
    path('my-blog/', views.MyBlog.as_view(), name = "myblog"),    
    path('Edit-blog/<pk>/', views.UpdateBlog.as_view(), name = "edit_blog"),    



]