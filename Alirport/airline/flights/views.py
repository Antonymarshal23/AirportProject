from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger, Airport


# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "Airports": Airport.objects.all(),
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    if request.method == "POST":
        # get the flight by flight_id
        flight = Flight.objects.get(pk=flight_id)
        # a form gonna have a passenger name when the users post which means
        # submit the passenger name this line of code will get the passenger
        # and add it into the add passenger list in the flight page
        # get the passenger which would be string and convert into integer
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # add a new passenger into the passengers flight
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
