from django.urls import path
from log import views

# Our Urls is a Part of our Controller as it handles Url Mapping to different
urlpatterns = [
    # in the code down below we can see that am i specifying a url
    # that my firstDjangoProject would use when someone request to go to
    # our logApp url
    path("", views.home_page, name="blog/homepage"),
    path("about/", views.about_page, name="blog/about-page"),
]
# Part of our WebApp
