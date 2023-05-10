from django.urls import path
from .views import get_descriptions_place

app_name = 'places'
urlpatterns = [
    path('<int:place_id>/', get_descriptions_place, name='place_details')
]
