from django.urls import path
from .views import get_desciptions_place

app_name = 'places'
urlpatterns = [
    path('<int:place_id>/', get_desciptions_place, name='place_details')
]
