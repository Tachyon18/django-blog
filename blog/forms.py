from django.forms import ModelForm
from .models import Blogs

class Create(ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'body', 'slug', 'image']
