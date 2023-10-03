from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('reg', views.reg, name='reg')
]
