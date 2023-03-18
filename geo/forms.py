from django import forms


class Coords_send(forms.Form):
    longitude = forms.CharField()
    latitude = forms.CharField()
