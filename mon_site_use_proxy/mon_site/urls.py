from django.urls import path
from .views import home
import django_cas_ng.views

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    path('accounts/logout', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
    ]