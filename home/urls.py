from django.urls import path
from home.views import *
from admin_dashboard.views import contact_us_mail

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('services', ServicePageView.as_view(), name='service'),
    path('contact-us', ContactPageView.as_view(), name='contact'),
    path('gallery', GalleryPageView.as_view(), name='gallery'),
    path('mail/send', contact_us_mail, name='send_mail'),


]

