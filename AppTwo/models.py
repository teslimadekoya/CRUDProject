from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    date_of_birth = models.DateField()


    def __str__(self):
        return self.name