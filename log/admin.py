from django.contrib import admin
from .models import Post

# Register your models here | these is where we would register our models so
# that the show up in our admin page.

admin.site.register(Post)
