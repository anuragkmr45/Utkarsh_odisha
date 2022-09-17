from django.db import models

# Register your models here.

class Contact(models.Model):
    # name = models.CharField(max_length=122)

    def __str__(self):
        return self.name
    