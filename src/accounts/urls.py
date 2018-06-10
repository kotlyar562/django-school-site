from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from . forms import LoginUser

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='accounts/login.html',
                                      form_class=LoginUser), name='login'),
    path('edit/', views.edit, name='edit'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/', views.profile, name='profile'),
]
