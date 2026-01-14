from django.db import models

# Create your models here.
class BookCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Member(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    category = models.ForeignKey(
        BookCategory,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.full_name
