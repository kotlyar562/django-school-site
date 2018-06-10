from django.urls import path
from . import views


app_name = 'svedenia'
urlpatterns = (
    path('', views.index, name='index'),
    path('<slug:group_slug>/', views.group_view, name='group'),
)
