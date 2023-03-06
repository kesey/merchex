from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from listings.models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, 
                  "listings/band_list.html", 
                  {"bands": bands})

def band_detail(request, band_id):
    # band = Band.objects.get(id=band_id)
    band = get_object_or_404(Band, pk=band_id) # display an error 404 if the band does not exist
    lists = Listing.objects.filter(band_id=band_id)
    return render(request,
                  "listings/band_detail.html",
                  {"band": band, "lists": lists})

def about(request):
    return render(request, "listings/about.html")

def contact(request):
    return render(request, "listings/contact.html")

def list(request):
    lists = Listing.objects.all()
    return render(request, 
                  "listings/list_list.html", 
                  {"lists": lists})

def list_detail(request, list_id):
    list = get_object_or_404(Listing, pk=list_id)
    return render(request,
                  "listings/list_detail.html",
                  {"list": list})
