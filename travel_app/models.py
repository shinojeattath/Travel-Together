from django.db import models

# Create your models here.
class review(models.Model):
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30, null = True)
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
    sub_places = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=30, null = True)
    date_from = models.DateField(null=True)
    date_to = models.DateField(null=True)
    no_of_travellers = models.CharField(max_length=30, null=True)


class sub_places(models.Model):
    main_place = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

class profile_photo(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='profile_photo/')