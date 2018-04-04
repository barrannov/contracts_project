from . import views
from django.urls import path
from django.contrib.auth.views import logout

app_name = 'contracts'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('registration_form/', views.UserFormView.as_view(), name='registration_form'),
    path('create/', views.CreateContract.as_view(), name='create'),
    path('my-contracts/', views.MyContracts.as_view(), name='my-contracts'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', logout, {'next_page': '/'}, name='logout')
]