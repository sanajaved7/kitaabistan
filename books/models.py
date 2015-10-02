from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=75)
    owned = models.BooleanField()
    to_read = models.BooleanField()

    def __str__(self):
        return self.title + " by " + self.author

    class Meta:
        unique_together = (("title", "author"),)
