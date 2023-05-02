from django.contrib import admin
from .models import Places, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
