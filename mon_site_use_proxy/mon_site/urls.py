from django.urls import path
from .views import home, login
import django_cas_ng.views

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    ]