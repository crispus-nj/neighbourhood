from django.db import models
from accounts.models import UserAccount

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='user')
    image = models.ImageField()
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Business(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='location')
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=70)
    county = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    people = models.ManyToManyField(UserAccount, blank=True, null=True, related_name='people')
    business = models.ManyToManyField(Business, blank=True, null=True, related_name='business')

    def __str__(self):
        return self.name

class Profile(models.Model):
    avatar = models.ImageField(null=True, default='avatar.svg')
    bio = models.TextField(blank=True, null=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='users')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='mtaani')

    def __str__(self):
        return self.user.username