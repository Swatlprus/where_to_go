from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Places, Image


def get_preview(Image):
    return format_html(
        '<img src="{url}" style="max-width: 200px; max-height: 200px;" />'
        .format(url=Image.img.url)
    )


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = [get_preview]
    extra = 1


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = [get_preview]
