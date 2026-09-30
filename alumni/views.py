from django.shortcuts import render

from alumni.models import Alumnus

# Create your views here.


def home(request):
    return render(request, "alumni/home.html")


def alumni_list(request):
    alumni = Alumnus.objects.all()
    return render(request, "alumni/alumni_list.html", {"alumni": alumni})
