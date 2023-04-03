from django.db import models

# Create your models here.

class Students(models.Model):
    gender_choices=(
        ('male', 'Male'),
        ('female', 'Female')
    )



    firstName = models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    phonenumber=models.CharField(max_length=20)
    address=models.TextField(max_length=100)
    gender=models.CharField(max_length=10, choices=gender_choices, default='male')

    def __str__(self):
        return self.lastname

