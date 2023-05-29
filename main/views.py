from django.shortcuts import render
from .models import Blog, Category

          

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home = True),
        "categories":Category.objects.all()
    }
    return render(request,template_name='main/index.html',context=context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories":Category.objects.all()
    }
    return render(request,template_name='main/blogs.html',context=context)

def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request,template_name='main/blog-detail.html',
                  context={'blog':blog})

def blogs_by_category(request,slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories":Category.objects.all(),
        "selected_category":slug,
    }
    return render(request,'main/blogs.html',context)