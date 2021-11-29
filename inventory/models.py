from django.db import models

# Create your models here.

class AllModels(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class meta:
        abstract = True

class Author(AllModels):
    full_name = models.CharField(max_length=500)
    dob = models.DateField()
    class meta:
        ordering = ["full_name"]


class Book(AllModels):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class meta:
        ordering = ["title"]

    #def __init__(self, title, author_id,):
    #    super().__init__(*args, **kwargs)