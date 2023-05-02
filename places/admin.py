from django.contrib import admin
from django.utils.html import format_html
from PIL import Image
from .models import Places, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height=200 />'
                           .format(
                                    url=obj.img.url,
                                    width=(obj.img.width/(obj.img.height/200)),
                                    ))


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
