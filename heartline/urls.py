from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bp/<int:entry_id>/', views.bp_detail, name='bp_detail'),
]