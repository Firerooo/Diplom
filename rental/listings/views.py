from django.shortcuts import render

def home(request):
    return render(request, 'listings/home.html')

def about(request):
    return render(request, 'listings/about-us.html')

def privacy(request):
    return render(request, 'listings/privacy-policy.html')

def apartments(request):
    return render(request, 'listings/apartments.html')

def reviews(request):
    return render(request, 'listings/reviews.html')
