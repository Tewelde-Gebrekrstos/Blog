from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import BlogPost
import json 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def view_news(request):
    posts = BlogPost.objects.all().values()
    print(posts)
    return render(request, './blog/news.html', {'posts': posts})
def view_sports(request):
    posts = BlogPost.objects.filter(category="sport")
    print(posts)
    return render(request, './blog/sports.html', {'posts': posts})
def view_politics(request):
    posts = BlogPost.objects.filter(category="politics")
    print(posts)
    return render(request, './blog/politics.html', {'posts': posts})
def view_bussiness(request):
    posts = BlogPost.objects.filter(category="bussiness")
    print(posts)
    return render(request, './blog/bussiness.html', {'posts': posts})

def view_detail(request,id):
    post = BlogPost.objects.get(id=id)
    print(post)
    return render(request, './blog/viewPostDetail.html', {'post': post})
