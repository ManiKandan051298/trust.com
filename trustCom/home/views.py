from django.shortcuts import render
from django.http import HttpResponse
from create_post.models import Contactdetails
# Create your views here.

class basic_details:
    contact=Contactdetails.objects.get(id=1)
    trustMail=contact.trustMail
    trustAddress=contact.trustAddress
    trustOrg=contact.trustOrg
    trustPhonenumber=contact.trustPhonenumber
    trustFrontimage=contact.trustFrontimage

def index(request):
    b=basic_details()
    data={
        "trustMail":b.trustMail,
        "trustAddress":b.trustAddress,
        "trustOrg":b.trustOrg,
        "trustPhonenumber":b.trustPhonenumber,
        "trustFrontimage":b.trustFrontimage,
    }
    return render(request,"index/index.html",data)

def about(request):
    return render(request,"about/about.html")