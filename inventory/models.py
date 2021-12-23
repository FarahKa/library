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
    def __str__(self):
        return self.full_name


class Book(AllModels):
    title = models.CharField(max_length=500)
    author_field = models.ForeignKey(Author, on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    pages_read = models.IntegerField()
    class meta:
        ordering = ["title"]
    def __str__(self):
        return self.title

    #def __init__(self, title, author_id,):
    #    super().__init__(*args, **kwargs)