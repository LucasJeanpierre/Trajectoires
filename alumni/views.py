from django.shortcuts import get_object_or_404, render

from alumni.models import Alumnus

# Create your views here.


def home(request):
    return render(request, "alumni/home.html")


def alumni_list(request):
    alumni = Alumnus.objects.all()
    return render(request, "alumni/alumni_list.html", {"alumni": alumni})


def alumnus_detail(request, pk):
    alumnus = get_object_or_404(Alumnus.objects.prefetch_related("study_stages"), pk=pk)
    return render(request, "alumni/alumnus_detail.html", {"alumnus": alumnus})
