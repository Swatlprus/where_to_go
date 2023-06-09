import requests
from django.core.management.base import BaseCommand
from urllib.parse import unquote
from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
import os

from places.models import Places


class Command(BaseCommand):
    help = 'Добавление данных о гео-точках'

    def add_arguments(self, parser):
        parser.add_argument('url', default=False,
                            help='Ссылка на JSON с данными')

    def handle(self, *args, **options):
        url = options['url']
        geo_point = requests.get(unquote(url))
        place = geo_point.json()
        try:
            point_place, created = Places.objects.get_or_create(
                title=place['title'],
                lng=place['coordinates']['lng'],
                lat=place['coordinates']['lat'],
                defaults={
                    'description_short': place.get('description_short', ''),
                    'description_long': place.get('description_long', ''),
                }
            )
            if not created:
                return
            for count, img_url in enumerate(place['imgs']):
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                content_file = ContentFile(
                    img_response.content,
                    name=os.path.basename(img_url)
                )
                point_place.images.create(
                    places=point_place,
                    img=content_file,
                    position=count
                )
        except MultipleObjectsReturned:
            print('Объектов с такими данными несколько.')
