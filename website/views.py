from django.shortcuts import render
from django.http import HttpResponse


# Views used to direct user to relevant page

def home(request):
    """
    Function directs user to homepage
    """
    return render(request,'website/index.html')

def about_us(request):
    """
    Function directs user to about us page
    """
    return render(request,'website/about_us.html')

def shop(request):
    """
    Function directs user to shop page
    """
    return render(request,'website/shop.html')

def contact(request):
    """
    Function directs user to contact us page
    """
    return render(request,'website/contact_us.html')

