from django.contrib import admin
from .models import Author
from .models import Book
from .models import Bookinstance
from .models import Genre
# Register your models here.

#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(Bookinstance)
#admin.site.register(Genre)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    
    fields = [
        'first_name',
        'last_name',
        ('date_of_birth', 'date_of_death')
    ]

class BookInstanceInline(admin.TabularInline):
    model = Bookinstance


    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
    
    
    def display_genre(self, obj):    
        return ', '.join([genre.name for genre in obj.genre.all()[:3] ])
    
    display_genre.short_description = 'Genre'
    

@admin.register(Bookinstance)
class BookinstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields' : ('book','imprint','id')
        }),
        ('availablity', {
            'fields' : ('status', 'due_back')
        })
    )