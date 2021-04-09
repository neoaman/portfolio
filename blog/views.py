from django.shortcuts import render
from utility.apps import mongodb
from .serializers import BlogPostSerializer
from .forms import BlogForm

from markdown import markdown

# Create your views here.
def home(request):
    collection = mongodb(use="blog")
    post = [ BlogPostSerializer(i).data for i in collection.filter({}) ]

    context = {
        "post":post,
    }

    return render(request,'blog/home.html',context=context)

def update(request,postId):
    collection = mongodb(use="blog")
    
    context = {
        "blog_form":BlogForm(collection.get({"postId":postId})),
    }

    return render(request,'blog/home.html',context=context)

def add(request):
    
    context = {
        "blog_form":BlogForm(),
    }

    return render(request,'blog/home.html',context=context)
