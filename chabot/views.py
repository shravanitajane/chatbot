from django.shortcuts import render, get_object_or_404, redirect
from .models import BookTrip, Facilities
from .forms import BookTripForm, FacilitiesForm, CancelTripForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'base.html')

# BookTrip CRUD operations
def booktrip_list(request):
    trips = BookTrip.objects.all()
    return render(request, 'booktrip_list.html', {'trips': trips})

def booktrip_detail(request, pk):
    trip = get_object_or_404(BookTrip, pk=pk)
    return render(request, 'booktrip_detail.html', {'trip': trip})

def booktrip_create(request):
    if request.method == "POST":
        form = BookTripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = BookTripForm()
    return render(request, 'base.html', {'form': form})

def booktrip_update(request, pk):
    trip = get_object_or_404(BookTrip, pk=pk)
    if request.method == "POST":
        form = BookTripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = BookTripForm(instance=trip)
    return render(request, 'base.html', {'form': form})

def booktrip_delete(request, pk):
    trip = get_object_or_404(BookTrip, pk=pk)
    if request.method == "POST":
        trip.delete()
        return redirect('base')
    return render(request, 'base.html', {'trip': trip})

def booktrip_cancel(request):
    if request.method == "POST":
        form = CancelTripForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            trip = BookTrip.objects.filter(email=email).first()
            if trip:
                trip.delete()
                messages.success(request, 'Your trip has been canceled.')
            else:
                messages.error(request, 'No trip found with this email.')
            return redirect('base')
    else:
        form = CancelTripForm()
    return render(request, 'base.html', {'form': form})

# Facilities CRUD operations
def facilities_list(request):
    facilities = Facilities.objects.all()
    return render(request, 'facilities_list.html', {'facilities': facilities})

def facilities_detail(request, pk):
    facility = get_object_or_404(Facilities, pk=pk)
    return render(request, 'facilities_detail.html', {'facility': facility})

def facilities_create(request):
    if request.method == "POST":
        form = FacilitiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facilities_list')
    else:
        form = FacilitiesForm()
    return render(request, 'facilities_form.html', {'form': form})

def facilities_update(request, pk):
    facility = get_object_or_404(Facilities, pk=pk)
    if request.method == "POST":
        form = FacilitiesForm(request.POST, instance=facility)
        if form.is_valid():
            form.save()
            return redirect('facilities_list')
    else:
        form = FacilitiesForm(instance=facility)
    return render(request, 'facilities_form.html', {'form': form})

def facilities_delete(request, pk):
    facility = get_object_or_404(Facilities, pk=pk)
    if request.method == "POST":
        facility.delete()
        return redirect('facilities_list')
    return render(request, 'facilities_confirm_delete.html', {'facility': facility})

