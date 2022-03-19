from django.db import models
from accounts.models import UserAccount

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Location(models.Model):
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=80)
    people = models.ManyToManyField(UserAccount, blank=True, null=True, related_name='people')

    def __str__(self):
        return self.name

class Business(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    loaction = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name