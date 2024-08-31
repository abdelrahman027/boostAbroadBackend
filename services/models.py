from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField(max_length=1000)
    image = models.ImageField(upload_to='service/', default='service/default-service.jpg',blank=True,null=True)

    def __str__(self) :
        return self.title
    


class Location(models.Model):
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    phone=models.CharField(max_length=100,null=True,blank=True)
    whats_link=models.CharField(max_length=1000,null=True,blank=True)

    address=models.CharField(max_length=512)
    district=models.CharField(max_length=100)
    location= models.TextField(max_length=3000)
    location_image = models.ImageField(upload_to='locations/', default='locations/locations.jpg',blank=True,null=True)

    def __str__(self) :
        return self.country + self.state



class Event(models.Model):
    country=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()
    address=models.CharField(max_length=512)
    description= models.TextField(max_length=3000)
    event_image = models.ImageField(upload_to='events/', default='events/event1.jpg',blank=True,null=True)

    def __str__(self) :
        return self.name +"-"+self.country
    


class knowledgehub(models.Model):
    country=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    event_date = models.DateField()
    address=models.CharField(max_length=512)
    description= models.TextField(max_length=3000)
    knowledge_image = models.ImageField(upload_to='knowledge/', default='knowledge/knowledge1.jpg',blank=True,null=True)

    def __str__(self) :
        return self.name +"_"+self.country