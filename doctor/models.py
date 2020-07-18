from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class extendedUser(models.Model):
    mobileNumber = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 10)
    user = models.OneToOneField(User,on_delete = models.CASCADE)