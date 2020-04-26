
from django.db import models

class Klient(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=150)
    miasto = models.CharField(max_length=50)
    ulica = models.CharField(max_length=50)

class Bilet(models.Model):
    id=models.AutoField(primary_key=True)
