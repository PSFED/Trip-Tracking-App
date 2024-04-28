from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Trip, Note


class HomeView(TemplateView):
    template_name = 'trip/index.html'


def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {
        'trips': trips,
    }
    return render(request, 'trip/trip_list.html', context)
