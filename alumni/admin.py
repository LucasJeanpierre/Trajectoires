from django.contrib import admin

from .models import Alumnus

# Register your models here.


@admin.register(Alumnus)
class AlumnusAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "graduation_year")
    search_fields = ("first_name", "last_name")
    list_filter = ("graduation_year",)
