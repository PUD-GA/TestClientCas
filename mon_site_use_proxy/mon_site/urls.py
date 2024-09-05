from django.urls import path
from .views import home, login

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login', login , name='cas_ng_login'),
    ]