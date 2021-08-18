from datetime import timedelta

from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='users_avatar',
        blank=True
    )

    age = models.PositiveIntegerField(
        verbose_name='возраст',
        default=18
    )

    activation_key = models.CharField(
        max_length=128,
        blank=True
    )

    activation_key_expires = models.DateTimeField(
        default=(now() + timedelta(hours=48))
    )

    def is_activation_key_expires(self):
        return now() >= self.activation_key_expires

class ShopUserprofile(models.Model):
    MALE = 'M'
    FEMALE = "Ж"

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'Ж')
    )

    user = models.OneToOneField(
        ShopUser,
        unique=True,
        null=False,
        db_index=True,
        on_delete=models.CASCADE
    )

    tagline = models.CharField(
        verbose_name='тэги',
        max_length=128,
        blank=True,
    )

    about_me = models.TextField(
        verbose_name='о себe',
        max_length=512,
        blank=True
    )

    gender = models.CharField(
        verbose_name='',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
    )
