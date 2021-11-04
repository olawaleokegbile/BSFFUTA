from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('signup', views.signup, name='signup'),
    #path('login', views.login, name='login'),
    path('my_profile', views.profile_form, name='profile-form'),
    path('search_members', views.search_members, name='search-members'),
    path('all_members', views.members_list, name='members-list'),
]
