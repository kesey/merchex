from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandCreateForm, ListCreateForm
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

def band_update(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    if request.method == "POST":
        formu = BandCreateForm(request.POST, instance=band)
        if formu.is_valid():
            formu.save()
            return redirect("band-detail", band.id)
    else:
        formu = BandCreateForm(instance=band) # create a Band form fill with the band that we want to update

    return render(request,
                  "listings/band_update.html",
                  {"formulaire": formu})

def band_delete(request, band_id):
    band = get_object_or_404(Band, pk=band_id)

    if request.method == "POST":
        band.delete()
        return redirect("band-list")
    
    return render(request,
                  "listings/band_delete.html",
                  {"band": band})

def contact(request):
    if request.method == "POST":
        formu = ContactUsForm(request.POST) # if the form has been submit (POST method) populate input with data
        if formu.is_valid():
            send_mail(
                subject=f"Message from {formu.cleaned_data['name']} via Merchex Contact Us Form",
                message=formu.cleaned_data["message"],
                from_email=formu.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"]
            )
            return redirect("email-sent") # redirection to confirmation page (with name=email-sent)
    else:
        formu = ContactUsForm() # if you arrive on this view (GET method) leave the input blank

    return render(request,
                  "listings/contact.html",
                  {"formulaire": formu})

def band_create(request):
    if request.method == "POST":
        formu = BandCreateForm(request.POST)
        if formu.is_valid():
            band = formu.save() # save instance of Band in database and return it
            return redirect("band-detail", band.id) # pass argument to url
    else:
        formu = BandCreateForm()

    return render(request, 
                  "listings/band_create.html",
                  {"formulaire": formu})

def about(request):
    return render(request, "listings/about.html")

def email_sent(request):
    return render(request, "listings/email_send_confirmation.html")

def list(request):
    ads = Listing.objects.all()
    return render(request, 
                  "listings/list_list.html", 
                  {"ads": ads})

def list_detail(request, list_id):
    ad = get_object_or_404(Listing, pk=list_id)
    return render(request,
                  "listings/list_detail.html",
                  {"ad": ad})

def list_create(request):
    if request.method == "POST":
        formu = ListCreateForm(request.POST)
        if formu.is_valid():
            ad = formu.save()
            return redirect("list-detail", ad.id)
    else:
        formu = ListCreateForm()

    return render(request, 
                  "listings/list_create.html",
                  {"formulaire": formu})

def list_update(request, list_id):
    ad = get_object_or_404(Listing, pk=list_id)

    if request.method == "POST":
        formu = ListCreateForm(request.POST, instance=ad)
        if formu.is_valid:
            formu.save()
            return redirect("list-detail", ad.id)
    else:
        formu = ListCreateForm(instance=ad)

    return render(request,
           "listings/list_update.html",
           {"formulaire": formu})

def list_delete(request, list_id):
    ad = get_object_or_404(Listing, pk=list_id)

    if request.method == "POST":
        ad.delete()
        return redirect("list-list")
    
    return render(request,
                  "listings/list_delete.html",
                  {"ad": ad})