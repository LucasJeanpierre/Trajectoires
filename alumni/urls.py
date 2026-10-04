from django.urls import path

from . import views

app_name = "alumni"

urlpatterns = [
    path("", views.home, name="home"),
    path("alumni/", views.alumni_list, name="list"),
    path("alumni/<int:pk>/", views.alumnus_detail, name="detail"),
]
