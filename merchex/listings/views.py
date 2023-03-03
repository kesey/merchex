from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 
                  "listings/hello.html", 
                  {"bands": bands})

def about(request):
    return render(request, "listings/about.html")

def contact(request):
    return render(request, "listings/contact.html")

def list(request):
    ads = Listing.objects.all()
    return render(request, 
                  "listings/list.html", 
                  {"ads": ads})
