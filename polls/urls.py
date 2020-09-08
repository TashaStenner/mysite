from drjango.urls import path
from . import views

urlpatters = [
    path('', views.index, name='index')
]