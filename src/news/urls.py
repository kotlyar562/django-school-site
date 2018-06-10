from django.urls import path
from . import views

app_name = 'news'
urlpatterns = (
   path('', views.index, name='index'),
   path('<int:news_pk>/', views.news, name='news'),
   path('add/', views.add_news, name='add_news'),
   path('edit/<int:news_pk>)/', views.edit_news, name='edit_news'),
)
