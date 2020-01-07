# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blogs
from .forms import Create

def add_blog(request):
    if request.method == "POST":
        addBlog = Create(request.POST, request.FILES)
        if addBlog.is_valid():
            addBlog.save()
            return redirect('blog:blogHome')
    else:
      addBlog = Create()
      return render(request, 'blog/create.html', {'addBlog':addBlog})


def blogHome(request):
    blogs = Blogs.objects.all().order_by('date')
    return render(request, 'blog/blogHome.html', {'blogs':blogs})

def blog_detail(request,slug):
    blog = Blogs.objects.get(slug=slug)
    return render(request, 'blog/blog_detail.html', {'blog':blog})


def delete_blog(request, slug):
    delBlog = Blogs.objects.filter(slug=slug).delete()
    return redirect('blog:blogHome')
