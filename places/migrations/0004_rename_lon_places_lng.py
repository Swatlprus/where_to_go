# Generated by Django 3.2.10 on 2023-04-28 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20230428_0543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='places',
            old_name='lon',
            new_name='lng',
        ),
    ]
