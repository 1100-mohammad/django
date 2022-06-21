
from django.shortcuts import render
from .models import Author, Book, Bookinstance, Genre
# Create your views here.

def index(request): 
    
    num_books = Book.objects.all().count()
    num_instance = Bookinstance.objects.all().count()
    num_instance_available = Bookinstance.objects.filter(status__exact = 'a').count()
    num_author = Author.objects.count()
    
    context = {
    'num_books' : num_books,
    'num_instance' : num_instance,
    'num_instance_available' : num_instance_available,
    'num_author' : num_author
    }
    
    return render(request, 'index.html', context)




