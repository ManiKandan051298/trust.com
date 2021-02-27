from django.shortcuts import render,HttpResponse

# Create your views here.
def login(request):
    return render(request,'Admin/adminLogin.html')

def trust_admin_login(request):
    if request.method =="POST":
        email=request.POST.get('adminGmail')
        password=request.POST.get('adminPassword')
        print(email,password)
        if email=="1@gmail.com" and password =='hello':
            data={
                "email":email,
                "password":password
            }
            return render(request,"admin_html/addimage.html",data)
        else:
            return render(request,"Admin/adminLogin.html",{"msg":"Incorrect Details"})

    else:            
        return render(request,"Admin/adminLogin.html",{"msg":"Please check serverside"})


def addimage(request):
    return render(request,'admin_html/addimage.html')


def addwhatwedo(request):
    return render(request,'admin_html/addwhatwedo.html')

def headingcontentimage(request):
    return render(request,'admin_html/headingcontentimage.html')
def managephotos(request):
    return render(request,'admin_html/managephotos.html')
def missionandvission(request):
    return render(request,'admin_html/missionandvission.html')
def frontimagechange(request):
    return render(request,'admin_html/frontimagechange.html')
def contactusform(request):
    return render(request,'admin_html/contactusform.html')

def listofwhatwedo(request):
    return render(request,'admin_html/listofwhatwedo.html')
