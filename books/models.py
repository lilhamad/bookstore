from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __unicode__(self):
        return self.firstname + " " + self.lastname

    def __str__(self):
        return self.firstname + " " + self.lastname



class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Rate(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    time = models.DateTimeField()
    message = models.CharField(max_length=255)
    rating = models.IntegerField(choices =((1, '1'), (2,'2'), (3, '3'), (4,'4'), (5,'5')))

    def __unicode__(self):
        return self.user.firstname + " : " + self.book.title

    def __str__(self):
        return self.user.username + " : " + self.book.title


