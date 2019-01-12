from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
# Models just refer to the Structure of how we want our Database structure
# to be like


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
