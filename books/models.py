from django.db import models

class Book(models.Model):
    """
    This model stores all the books and their pertaining information.
    Owned: Books that you currently own. When filling out the form,
    if owned is not selected, the book is added to the "Want to Buy"
    list on the home page.
    To_read: Books that are on your to-read list. If "to-read" is not
    selected upon filling out the form, then the book is marked as
    "Books I have read".

    """
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=75)
    owned = models.BooleanField()
    to_read = models.BooleanField()

    def __str__(self):
        return self.title + " by " + self.author

    class Meta:
        """
        Prevent duplicate books by the same author being added into
        the database.
        """
        unique_together = (("title", "author"),)
