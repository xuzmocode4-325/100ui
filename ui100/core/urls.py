from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('payment', views.PatmentView.as_view(), name='payment')
]