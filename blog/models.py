# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to = 'media/', blank=True)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100]+ '...'
