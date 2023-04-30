from django.shortcuts import render
from places.models import Places


def show_maps(request):
    places = Places.objects.all()
    features = []

    for place in places:
        place = {
                "type": "Feature",
                "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
                },
                "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": "static/places/moscow_legends.json"
                }
                }
        features.append(place)

    data = {"maps" : {
            "type": "FeatureCollection",
            "features": features
            }}
    return render(request, 'index.html', context=data)
