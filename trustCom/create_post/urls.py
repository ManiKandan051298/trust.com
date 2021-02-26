from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.login,name="login"),
    #trust_admin_login
    path('trust_admin_login/',views.trust_admin_login,name="trust_admin_login"),
]