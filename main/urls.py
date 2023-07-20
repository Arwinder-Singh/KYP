from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dept/<str:department>/',views.dept,name='dept'),
    path('team/',views.team,name='team'),
    path('contact/',views.contact,name='contact'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('search/',views.get_names,name='get_names'),
    path('temp/',views.temp,name='temp'),
    path('random/<int:key>/',views.random,name="random"),
    
    


]
