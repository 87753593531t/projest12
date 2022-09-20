from django.db import models


class UserN(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Name',
    )
    surname = models.CharField(
        max_length=50,
        verbose_name='Surname'
    )

    class Meta:
        verbose_name = 'UserN'
        verbose_name_plural = 'UserNs'
        ordering = ('id',)
