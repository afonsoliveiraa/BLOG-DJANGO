from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    content = models.TextField()
    date_create = models.DateField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def get_tags(self):
        return ", ".join([str(name) for name in self.tags.all()])

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    date_create = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(self.content)
