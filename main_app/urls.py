from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('instruments/', views.instruments_index, name='instruments_index'),
    path('instruments/<int:instrument_id>/', views.instruments_detail, name='instruments_detail'),
]