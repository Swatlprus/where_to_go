from django.urls import path
from .views import get_id_place

app_name = 'places'
urlpatterns = [
    path('<int:place_id>/', get_id_place, name='place_details')
]
