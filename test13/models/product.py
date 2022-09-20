from django.db import models

from test13.models import UserN


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='ПродуКТ',
    )
    description = models.CharField(
        max_length=255,
        verbose_name='описание',
        blank=True,
        # null=True
    )
    quality = models.CharField(
        max_length=100,
        verbose_name='каЧестВо',
        default='quality NONE'
    )
    usern = models.ForeignKey(
        UserN,
        on_delete=models.CASCADE,
        verbose_name='ЮЗЕР'
    )

    class Meta:
        verbose_name = 'ПроДукТ'
        verbose_name_plural = 'ПроДукТы'
