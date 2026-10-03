from django.contrib import admin

from .models import Alumnus, BacSeries

# Register your models here.


@admin.register(BacSeries)
class BacSeriesAdmin(admin.ModelAdmin):
    list_display = ("name", "period", "display_order")
    ordering = ("display_order", "name")
    search_fields = ("name", "period")


@admin.register(Alumnus)
class AlumnusAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "graduation_year", "bac_series")
    search_fields = ("first_name", "last_name")
    list_filter = ("graduation_year", "bac_series")
    autocomplete_fields = ("bac_series",)
