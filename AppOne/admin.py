from django.contrib import admin
from AppOne.models import Books

# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    search_fields = ('title', 'author')

admin.site.register(Books, BooksAdmin)