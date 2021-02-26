from django.shortcuts import render,HttpResponse

# Create your views here.
def login(request):
    return render(request,'adminLogin.html')

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
            return render(request,"Admin/adminHome.html",data)
        else:
            return render(request,"adminLogin.html",{"msg":"Incorrect Details"})

    else:            
        return render(request,"adminLogin.html",{"msg":"Please check serverside"})