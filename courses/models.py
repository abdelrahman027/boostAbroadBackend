from django.db import models

# Create your models here.




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
    university=models.ForeignKey(University,models.SET_NULL,null=True)
    def __str__(self):
        return self.name