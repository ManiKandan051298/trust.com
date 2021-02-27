from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.login,name="login"),
    #trust_admin_login
    path('trust_admin_login/',views.trust_admin_login,name="trust_admin_login"),
    path('addimage/',views.addimage,name="addimage"),
    path('listofwhatwedo/',views.listofwhatwedo,name="listofwhatwedo"),

    path('addwhatwedo/',views.addwhatwedo,name="addwhatwedo"),
    path('headingcontentimage/',views.headingcontentimage,name="headingcontentimage"),
    path('managephotos/',views.managephotos,name="managephotos"),
    path('missionandvission/',views.missionandvission,name="missionandvission"),
    path('frontimagechange/',views.frontimagechange,name="frontimagechange"),
    path('contactusform/',views.contactusform,name="contactusform"),
]