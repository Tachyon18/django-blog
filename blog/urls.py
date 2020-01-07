from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.blogHome, name="blogHome"),
    url(r'^add-blog/$', views.add_blog, name="add_blog"),
    url(r'^(?P<slug>[\w-]+)/$', views.blog_detail, name="detail"),
    url(r'^delete/(?P<slug>[\w-]+)/$', views.delete_blog, name="delete"),
    
]
