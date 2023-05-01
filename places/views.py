from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Places, Image


def get_id_place(requests, place_id):
    place = get_object_or_404(Places, pk=place_id)
    imgs = Image.objects.filter(places=place_id)
    images = []
    for img in imgs:
        image = Image.objects.get(pk=img.pk)
        images.append(image.img.url)

    json = {
        "title": place.title,
        "imgs": images,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng,
        }

    }
    return JsonResponse(json, json_dumps_params={'indent': 2,
                                                 'ensure_ascii': False})
