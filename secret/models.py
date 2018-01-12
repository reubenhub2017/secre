from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    
    def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)
            

    def __str__(self):
        return self.title
    
    