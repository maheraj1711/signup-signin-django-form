from django.contrib import admin
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logedout/', logedout, name='logedout'),
    path('home/', home, name='home'),
]
