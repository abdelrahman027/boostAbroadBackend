from django.db import models

# Create your models here.

class Requirements(models.TextChoices):
    Consolidated_Marksheets="Consolidated Marksheets"
    Letter_of_Reference="Letter of Reference"
    Personal_Statement="Personal Statement"
    Semester_Marksheetsn="Semester Marksheets"
    Passport="Passport"
    Provisional_Certificate="Provisional Certificate"
    I20 ="I20"



class University(models.Model):
    name = models.CharField(max_length=100)
    shortName = models.CharField(max_length=10,null=True,blank=True)
    location = models.CharField(max_length=500,null=True,blank=True)
    country = models.CharField(max_length=50,default="UK")
    city = models.CharField(max_length=50,default="London")
    description= models.TextField(max_length=1000)
    image = models.ImageField(upload_to='universities/', default='universities/default-service.jpg',blank=True,null=True)

    def __str__(self) :
        return self.name
    

class Program(models.Model):
    name = models.CharField(max_length=100)
    given_degree =models.CharField(max_length=100)
    duration_from =models.IntegerField()
    duration_to =models.IntegerField()
    first_sem_date=models.CharField(max_length=100)
    second_sem_date=models.CharField(max_length=100)
    fees = models.CharField(max_length=50)
    about = models.TextField(max_length=3000,blank=True,null=True)
    Requirement1 = models.CharField(max_length=40,choices=Requirements.choices,blank=True,null=True)
    Requirement2 = models.CharField(max_length=40,choices=Requirements.choices,blank=True,null=True)
    Requirement3 = models.CharField(max_length=40,choices=Requirements.choices,blank=True,null=True)
    Requirement4 = models.CharField(max_length=40,choices=Requirements.choices,blank=True,null=True)
    Requirement5 = models.CharField(max_length=40,choices=Requirements.choices,blank=True,null=True)
    Requirement6 = models.CharField(max_length=40,choices=Requirements.choices,blank=True,null=True)
    Requirement7 = models.CharField(max_length=40,choices=Requirements.choices,blank=True,null=True)


    university=models.ForeignKey(University,models.SET_NULL,null=True)
    def __str__(self):
        return self.name
    

class Destination(models.Model):
    number = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    country = models.CharField(max_length=50,default="UK")
    city = models.CharField(max_length=50,default="London")
    continent = models.CharField(max_length=50,default="Europe")
    description= models.TextField(max_length=1000)
    image = models.ImageField(upload_to='destinations/', default='destinations/athens.png',blank=True,null=True)

    def __str__(self) :
        return self.Name
    