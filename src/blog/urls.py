from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = (
   path('', views.index, name='index'),
   path('<int:article_pk>/', views.article, name='article'),
   path('add/', views.add_article, name='add_article'),
   path('edit/<int:article_pk>/', views.edit_article, name='edit_article'),
)
