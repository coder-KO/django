from django.db import models
from django.urls import reverse
import uuid


# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=20,help_text='enter a book genre ')

    def __str__(self):
        return self.name

class Language(models.Model):
    lang=models.CharField(max_length=100,help_text="enter the languages in which the book is available")

    def __str__(self):
        return self.lang


class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    summary=models.TextField(max_length=1000,help_text='enter the brief summary of the book')
    isbn=models.CharField('ISBN',max_length=13,help_text='13 character <a href="http://www.isbn-international.org/content/whta-isbn">ISBN no </a>')
    genre=models.ManyToManyField(Genre,help_text='Select a genre for this book')
    language=models.ManyToManyField(Language,help_text='select the language in which book is available')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # returns the url to access a detailed record of this book
        return reverse('book-detail',args=[str(self.id)])

class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="unique id for the particular book across the library")
    book=models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True,blank=True)

    LOAN_STATUS=(
    ('m','Maintenance'),
    ('o','on loan'),
    ('a','Available'),
    ('r','Reserved'),
    )

    status=models.CharField(
    max_length=1,
    choices=LOAN_STATUS,
    blank=True,
    help_text='Book availability'
    )

    class Meta:
        ordering=['due_back']
    def __str__(self):
        return f'{self.id} ({self.book.title})'



class Author(models.Model):
    first_name=models.CharField('First',max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True,blank=True)
    date_of_death=models.DateField('Died',null=True,blank=True)

    class Meta:
        ordering=['last_name','first_name']

    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name},{self.first_name}'
