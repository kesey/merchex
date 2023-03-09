from django import forms
from listings.models import Band, Listing

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BandCreateForm(forms.ModelForm):
    class Meta:
        model = Band # reuse model Band to create form
        fields = "__all__" # reuse all the fields in Band
        # exclude = ("active", "official_homepage") # only works if you delete fields = "__all__"
        # exclude fields must have default value or NULL enabled with null=True 

class ListCreateForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"


