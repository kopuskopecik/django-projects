from django.db import models

# Create your models here.



class Slot(models.Model):
    empty = models.BooleanField(default = True)


class Car(models.Model):
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE, null = True, blank = True)