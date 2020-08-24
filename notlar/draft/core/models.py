from django.db import models

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    active = models.BooleanField(default = False)
    
    def __str__(self):
        return self.title