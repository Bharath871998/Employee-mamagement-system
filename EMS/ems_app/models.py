from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choice = (
        ("Male", "M"),
        ("Female", "F")
    )
    gender = models.CharField(max_length=20, choices= gender_choice)
    joining_date = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)
    education = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    


    
    
    