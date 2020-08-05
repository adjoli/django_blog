from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=40),
    title = models.CharField(max_length=100),
    content = models.CharField(max_length=255),
    date_posted = models.DateField(auto_now_add=True)

    objetos = models.Manager()
