from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('payment', views.PatmentView.as_view(), name='payment'),
    path('hero', views.HeroView.as_view(), name='hero'),
    path('calculator', views.CalculatorView.as_view(), name='calculator'),
]