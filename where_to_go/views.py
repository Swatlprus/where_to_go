from django.shortcuts import render
from places.models import Places
from django.urls import reverse
from places.views import get_id_place


def show_maps(request):
    places = Places.objects.all()
    features = []

    for place in places:
        place = {
                "type": "Feature",
                "geometry":
                {
                 "type": "Point",
                 "coordinates": [place.lng, place.lat]
                },
                "properties": {
                 "title": place.title,
                 "placeId": place.id,
                 "detailsUrl": reverse('places:place_details', kwargs={
                                                        "place_id": place.id}),
                }
                }
        features.append(place)

    data = {"maps": {
            "type": "FeatureCollection",
            "features": features
            }}
    return render(request, 'index.html', context=data)
