# Generated by Django 3.2.18 on 2023-05-05 10:56

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_image_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterField(
            model_name='image',
            name='places',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.places', verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='places',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Полное описание'),
        ),
    ]
