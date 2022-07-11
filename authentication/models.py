from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    System User
    """

    name = models.CharField(_('name'), max_length=150, blank=True)
    bio = models.CharField(_('bio'), max_length=150, blank=True)
    image = models.ImageField(_('image'), upload_to='media/profiles/images/', blank=True)
    phone = models.CharField(_('phone'), max_length=150, blank=True)
    location = models.CharField(_('location'), max_length=150, blank=True)
    date_birth = models.DateField(_('birth date'), blank=True, null=True)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)
