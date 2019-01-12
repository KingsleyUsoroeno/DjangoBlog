from django.shortcuts import render
from .models import Post

# Create your views here.
# View is what our Users Will see on their Browser


def home_page(request):
    # in order to do a Database query on our Django Database we do this --->
    context = {"user_post": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about_page(request):
    return render(request, "blog/about.html", {"title": "About"})
