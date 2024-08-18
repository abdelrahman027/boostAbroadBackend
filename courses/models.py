from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=100)
    shortName = models.CharField(max_length=10,null=True,blank=True)
    description= models.TextField(max_length=1000)
    image = models.ImageField(upload_to='universities/', default='universities/default-service.jpg',blank=True,null=True)

    def __str__(self) :
        return self.name +self.shortName