from . import views
from django.urls import path
from django.contrib.auth.views import logout, login

app_name = 'contracts'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('registration_form/', views.UserFormView.as_view(), name='registration_form'),
    path('login/', login, name='login'),
    path('logout/', logout, {'next_page': '/'}, name='logout')
]