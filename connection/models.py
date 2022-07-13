from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.models import User


class Connection(models.Model):
    followed = models.ForeignKey(User, related_name='followed_user', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Connection')
        verbose_name_plural = _('Connections')

    def __str__(self):
        return f'User {self.followed} followed by {self.follower}'
