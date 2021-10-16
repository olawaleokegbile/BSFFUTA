from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('contact_form', views.contact_form, name='contact-form'),
    path('base', views.base, name='base'),
]
