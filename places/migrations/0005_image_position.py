# Generated by Django 3.2.10 on 2023-05-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_rename_lon_places_lng'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Позиция фото'),
        ),
    ]
