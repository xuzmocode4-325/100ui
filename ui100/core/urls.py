from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('payment', views.PatmentView.as_view(), name='payment'),
    path('hero', views.HeroView.as_view(), name='hero'),
    path('calculator', views.CalculatorView.as_view(), name='calculator'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('settings', views.SettingsView.as_view(), name='settings'),
    path('404', views.NotFoundView.as_view(), name='404'),
    path('music', views.MusicView.as_view(), name='music'),
    path('social', views.SocialView.as_view(), name='social'),
    path('flash', views.FlashView.as_view(), name='flash'),
    path('commerce', views.CommerceView.as_view(), name='commerce'),
]