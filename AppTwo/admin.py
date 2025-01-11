from django.contrib import admin
from . models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')


admin.site.register(Author, AuthorAdmin)