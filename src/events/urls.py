from django.urls import path
from . import views


app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_event/', views.get_event),
    path('add_event/', views.add_event, name='add_event')
]
