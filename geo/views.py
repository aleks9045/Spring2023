from django.shortcuts import render
from .forms import Coords_send


def coords_send(request):
    if request.method == 'POST':
        coords_form = Coords_send(request.POST)
