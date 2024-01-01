from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category
# Create your views here.

data = {
    "blogs": [
        {
            "id": 1,
            "title": "Horoscope",
            "image": "data-science.svg",
            "is_active": True,
            "is_home": True,
            "description": "Successful category",
            "advisor": 0
        },
        {
            "id": 2,
            "title": "Animal Kingdom",
            "image": "data-science.svg",
            "is_active": True,
            "is_home": True,
            "description": "Successful category",
            "advisor": 0
        },
        {
            "id": 3,
            "title": "Love and Relationship",
            "image": "data-science.svg",
            "is_active": True,
            "is_home": False,
            "description": "Successful category",
            "advisor": 0
        }
    ] 
}



def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active = True, is_home = True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active = True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)
    

def blog_details(request,slug):
    blog = Blog.objects.get(slug = slug)
    return render(request, "blog/blog_details.html", {
        "blog" : blog 
    })    

def about(request):
    return render(request, "blog/about.html")

def become_advisor(request):
    return render(request, "blog/become_advisor.html")

def blogs_by_category(request,slug):
    context = {
        "blogs": Blog.objects.filter(is_active = True, category__slug= slug),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)


# index de 555. satırdaki koda güzel bir video linki ekle
