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
        print(place['title'])
        try:
            point_place, created = Places.objects.get_or_create(
                                    title=place['title'],
                                    description_short=place['description_short'],
                                    description_long=place['description_long'],
                                    lng=place['coordinates']['lng'],
                                    lat=place['coordinates']['lat']
                                    )
            if created:
                for count, img_url in enumerate(place['imgs']):
                    img_response = requests.get(img_url)
                    img_response.raise_for_status()

                    image_field, image_created = point_place.images.get_or_create(position=count)
                    if image_created:
                        image_field.img.save(os.path.basename(img_url),
                                             ContentFile(img_response.content),
                                             save=True)

        except MultipleObjectsReturned:
            print('Объект с такими данным уже существует.')
