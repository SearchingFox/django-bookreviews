from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='books/images/')
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title