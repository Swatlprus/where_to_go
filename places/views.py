from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Places


def get_descriptions_place(requests, place_id):
    place = get_object_or_404(Places, pk=place_id)

    place_point = {
        'title': place.title,
        'imgs': [image.img.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
                    'lat': place.lat,
                    'lng': place.lng,
        }

    }
    return JsonResponse(place_point, json_dumps_params={
        'indent': 2,
        'ensure_ascii': False,
        }
    )
