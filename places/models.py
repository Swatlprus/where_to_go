from django.db import models
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.CharField(
        max_length=250,
        verbose_name='Краткое описание'
    )
    description_long = HTMLField(verbose_name='Полное описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(verbose_name='Изображение')
    places = models.ForeignKey(
        Places,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE
    )
    position = models.PositiveSmallIntegerField(
        verbose_name='Позиция фото',
        default=0,
        blank=True
    )

    class Meta:
        ordering = ['position', ]
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.id} {self.places.title}'
