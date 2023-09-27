from django.urls import path
from . import views

# provide app name
app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/',views.shop, name = 'shop'),
    path('aboutus/', views.about_us, name='about_us'),
    path('contactus/', views.contact, name = 'contact_us'),   
]



