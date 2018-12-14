from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True
    )
    phone = models.CharField(
        max_length=11,
        blank=True,
        null=True
    )

    # def __str__(self):
    #     return self.username
