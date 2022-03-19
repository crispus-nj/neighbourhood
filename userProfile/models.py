from django.db import models
from accounts.models import UserAccount
from neighbour.models import Location, Business

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)
    avatar = models.ImageField(null=True, default='avatar.svg')