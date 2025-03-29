from django.urls import path
from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about, name='about'),
    path('privacy-policy', views.privacy, name='privacy'),
    path('apartments', views.apartments, name='apartments'),
    path('reviews/', views.reviews_list, name='reviews_list'),
    path('add-review/', views.add_review, name='add_review'),
]
