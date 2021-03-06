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

    def get_absolute_url(self):
        return f'edit/{self.username}'

    def __str__(self):
        return 'Логин: {}{}'.format(self.username, ', superuser' if self.is_superuser else '')

    class Meta:
        ordering = ['-is_active', '-is_superuser', 'username']
