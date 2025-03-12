from django import forms
from .models import BookTrip, Facilities

class BookTripForm(forms.ModelForm):
    class Meta:
        model = BookTrip
        fields = ['name', 'email', 'phone', 'destination', 'date']

class FacilitiesForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = ['Dining_Options', 'Entertainment_Activities', 'Accommodation_Details']

class CancelTripForm(forms.Form):
    email = forms.EmailField()