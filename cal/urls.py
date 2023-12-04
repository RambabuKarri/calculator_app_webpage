from django.urls import path
from django.contrib import admin
from cal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greetings/', greetings, name='greetings'),
    path('calculation/', calculation, name='calculation'),
    
]
