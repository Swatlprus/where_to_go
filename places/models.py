from django.db import models
from django.urls import reverse


class Places(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.CharField(max_length=250,
                                         verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('place.views.get_id_place', args=[str(self.id)])

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    img = models.ImageField(verbose_name='Изображение')
    places = models.ForeignKey(Places, verbose_name='Место',
                               on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(verbose_name='Позиция фото',
                                                default=0,
                                                blank=True)

    def __str__(self):
        return f'{self.id} {self.places.title}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
