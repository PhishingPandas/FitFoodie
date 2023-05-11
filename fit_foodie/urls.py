from django.urls import path
from . import views

urlpatterns=[
    path('input/',views.food_input,name='input'),
    path('',views.home,name='home'),
    path('register/',views.signup,name='register'),
    path('login/',views.login,name='login'),
]