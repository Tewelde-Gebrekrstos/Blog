from django.contrib import admin
from .models import BlogPost
class BlogAdmin(admin.ModelAdmin):
  list_display = ("title", "content", "author","category","image","published_date")
  
admin.site.register(BlogPost, BlogAdmin)
# Register your models here.
