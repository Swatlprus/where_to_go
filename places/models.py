from django.db import models


class Places(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.CharField(max_length=250, verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    img = models.ImageField(verbose_name='Изображение')
    places = models.ForeignKey(Places, verbose_name='Место', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.places.title}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
