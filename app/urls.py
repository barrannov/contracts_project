from . import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('registration_form/', views.UserFormView.as_view(), name='registration_form')
]