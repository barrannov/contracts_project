from . import views
from django.urls import path

app_name = 'contracts'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('registration_form/', views.UserFormView.as_view(), name='registration_form')

]