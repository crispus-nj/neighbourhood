from django.db import models
from accounts.models import UserAccount
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='user')
    image = CloudinaryField("image")
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Business(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='author')
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='location')
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    image = CloudinaryField("image")

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(null=True, blank=True)
    people = models.ManyToManyField(UserAccount, blank=True, null=True, related_name='people')
    business = models.ManyToManyField(Business, blank=True, null=True, related_name='business')

    def __str__(self):
        return self.name

