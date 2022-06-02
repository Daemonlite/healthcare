from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Doctor(models.Model):
    BOOL=(
        ('available','available'),
        ('not_available','not_available')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    years_of_experience = models.IntegerField(default=5)
    speciality = models.CharField(max_length=150)
    is_available = models.CharField(choices=BOOL, max_length=100)

    def __str__(self):
        return self.name

class Hospital_card(models.Model):
     CARDS=(
         ('NULL','NULL'),
         ('NATIONAL','NATIONAL'),
         ('PRIVATE','PRIVATE'),
     )

     full_name = models.CharField(max_length=150)
     age = models.IntegerField(default=18)
     email = models.EmailField()
     residence = models.CharField(max_length=200)
     with_insurance = models.BooleanField(default=False)
     id_type = models.CharField(choices=CARDS,max_length=300)
     id_number = models.BigIntegerField()
     is_valid = models.BooleanField(default=False)

     def __str__(self):
         return self.full_name

class Complaint(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name