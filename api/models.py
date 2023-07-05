from django.db import models

# Create your models here.
# CATEGORY_CHOICES=("Birthday", "Sports", "Conferences","Expos","Concerts","Festivals","Performing Arts")
CATEGORY_CHOICES=(
(1,"Birthday"),
(2,"Sports"),
(3,"Conferences"),
(4,"Expos"),
(5,"Concerts"),
(6,"Concerts"),
(7,"Festivals"),
(8,"Performing Arts")
)

class Venue(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    capacity=models.IntegerField()
    amenities=models.CharField(max_length=500)
    availability=models.IntegerField(choices=((0,"Yes"),(1,"No")))
    
class Events(models.Model):
    title=models.CharField(max_length=50)
    description= models.CharField(max_length=400)
    date=models.DateField()
    time=models.TimeField()
    venue = models.ForeignKey(Venue,on_delete=models.CASCADE)
    category=models.IntegerField(choices=CATEGORY_CHOICES)
    active= models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-createdAt']
        def __str__(self):
            return self.title

class Registration(models.Model):
    name = models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    event = models.ForeignKey(Events,on_delete=models.CASCADE)
    status = models.IntegerField(choices=((0,"Reject"),(1,"Accept")))
