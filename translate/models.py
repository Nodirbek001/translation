from django.db import models

from django.utils.translation import gettext_lazy as _


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=30, verbose_name=_('Last Name'))
    email = models.EmailField(verbose_name=_('email'))

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
