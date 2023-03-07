from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from listings.models import Band, Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail

def band_list(request):
    bands = Band.objects.all()
    return render(request, 
                  "listings/band_list.html", 
                  {"bands": bands})

def band_detail(request, band_id):
    # band = Band.objects.get(id=band_id)
    band = get_object_or_404(Band, pk=band_id) # display an error 404 if the band does not exist
    lists = Listing.objects.filter(band_id=band_id) # get all the lists with a foreign key equal to band_id
    return render(request,
                  "listings/band_detail.html",
                  {"band": band, "lists": lists})

def about(request):
    return render(request, "listings/about.html")

def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST) # if the form has been submit (POST method) populate input with data
        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name']} via Merchex Contact Us Form",
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"]
            )
            return redirect('email-sent') # redirection to confirmation page (with name=email-sent)
    else:
        form = ContactUsForm() # if you arrive on this view (GET method) leave the input blank

    return render(request,
                  "listings/contact.html",
                  {"form": form})

def email_sent(request):
    return render(request, "listings/email_confirmation.html")

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
