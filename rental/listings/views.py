from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from django.core.paginator import Paginator


def home(request):
    reviews = Review.objects.select_related('user').order_by('created_at')[:3]
    return render(request, 'listings/home.html', {'reviews': reviews})

def about(request):
    return render(request, 'listings/about-us.html')

def privacy(request):
    return render(request, 'listings/privacy-policy.html')

def apartments(request):
    return render(request, 'listings/apartments.html')

def reviews(request):
    return render(request, 'listings/reviews.html')

def reviews_list(request):
    reviews = Review.objects.select_related('user').order_by('-created_at')
    paginator = Paginator(reviews, 5)
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    
    form = ReviewForm()
    return render(request, 'listings/reviews.html', {'page_obj': page_obj, 'form': form})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
    return redirect('listings:reviews_list')

