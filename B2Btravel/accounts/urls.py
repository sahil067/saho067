from django.contrib import admin
from django.urls import path, include
from accounts import views

# Django admin header customisation

admin.site.site_header = "Login to B2B TRAVEL"
admin.site.site_title = "Welcome to  Dashboard"
admin.site.index_title = "Welcome to B2B TRAVEL Portel"
urlpatterns = [
    path('', views.home, name='home'),
    path('Dashboard', views.about, name='Dashboard'),
    path('Online Booking', views.projects, name='Online Booking'),
    path('contact', views.contact, name='contact'),
]
