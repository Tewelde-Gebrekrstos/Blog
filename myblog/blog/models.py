from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class BlogPost(models.Model):
    CATEGORY_CHOICES = (
        ('sport', 'sport'),
        ('politics', 'politics'),
        ('bussiness', 'bussiness'),

    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='static/blogimages/')
    category=models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
    