from django.contrib.gis.db import models as geo_models
from django.contrib.gis.geos import Point
from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.models import User


class Media(models.Model):
    media_file = models.ImageField(_('file'), upload_to='media/profiles/media/')
    location = geo_models.PointField(_('location'), blank=True, default=Point(0, 0))  # or Point([])
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        verbose_name = _('Media File')
        verbose_name_plural = _('Media Files')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.OneToOneField(Media, on_delete=models.CASCADE)
    caption = models.CharField(_('caption'), max_length=2200, blank=True)
    location = geo_models.PointField(
        _('location'),
        blank=True,
        # patial_index=False,
        default=Point(0, 0),  # or Point([])
    )
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(_('comment'), max_length=2200, blank=True)
    reply = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        verbose_name = _('Reaction')
        verbose_name_plural = _('Reactions')
