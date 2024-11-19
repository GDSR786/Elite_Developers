from datetime import datetime

from django.db import models

from tinymce.models import HTMLField


# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    short_desc = models.TextField()
    content = HTMLField()
    url = models.SlugField()
    blog_img = models.ImageField(upload_to="blog-pics")
    banner_img = models.ImageField(upload_to="blog-pics")
    date_published = models.DateField()
    tags = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.title


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    plan = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.email}"


class NewsLetterModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.email}"


class CommentModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    blog = models.ForeignKey(
        to=BlogModel, verbose_name="Blog", on_delete=models.CASCADE
    )
    comment = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name} -------- {self.email}"
