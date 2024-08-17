from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField(max_length=1000)
    image = models.ImageField(upload_to='service/', default='service/default-service.jpg',blank=True,null=True)

    def __str__(self) :
        return self.title