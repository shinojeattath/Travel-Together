from django.db import models

# Create your models here.
class review(models.Model):
    name = models.CharField(max_length=30)
    review = models.CharField(max_length=300)

class travelling_place(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=30)

class hospital(models.Model):
    place = models.CharField(max_length=20)
    hospital_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

class travelling_user(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=30)
    P = models.CharField(max_length=5)