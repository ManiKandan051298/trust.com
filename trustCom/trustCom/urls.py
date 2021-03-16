from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import handler404, handler500,handler400
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('trustmanager/login/',include("create_post.urls"))
]


handler404 = 'home.views.error_404_view'
#handler500 = 'home.views.error_500_view'

