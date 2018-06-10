from django.urls import path

from . import views

urlpatterns = (
    path('<slug:page_slug>/', views.page, name='page'),
)
