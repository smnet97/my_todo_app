from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    user_img = models.ImageField(upload_to='user/', default='/icon/user_icon.png')
