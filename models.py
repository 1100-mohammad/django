import uuid 
from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length= 200, help_text= 'enter a book genre(e.g. Science Fiction, French Poetry etc.)')
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text= 'enter a brief description of the book')
    isbn = models.CharField(max_length=13 , help_text= '13 character')
    genre = models.ManyToManyField(Genre, help_text= 'select agenre for this book')
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null =True)
    

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null = True,blank = True)
    date_of_death = models.DateField('Died',null= True , blank=True)
    
    class Meta:
        ordering = ["-last_name", "first_name"]
    
    
    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)
    
class Bookinstance(models.Model):
    id = models.UUIDField(primary_key= True, default=uuid.uuid4,
    help_text = 'unique id for this particular book across whole library ')
    book = models.ForeignKey('book', on_delete = models.SET_NULL, null = True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null = True, blank = True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'on loan'),
        ('a', 'available'),
        ('r', 'reserved'),
    )

    status = models.CharField(max_length = 1 , choices = LOAN_STATUS, blank = True, default= 'm',help_text = 'book availabity')


class Meta:
    ordering = ["due_back"]
    
    def __str__(self):
        return '{0} ({1})'.format(self.id, self.book.title)
