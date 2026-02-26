from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    BPEntryListView,
    BPEntryDetailView, 
    BPEntryCreateView,
    BPEntryUpdateView,
    BPEntryDeleteView,
    register,
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='heartline/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='heartline/logout.html'), name='logout'),
    path('register/', register, name ='register'),
    path('bp/new/', BPEntryCreateView.as_view(), name='bpentry-create'),
    path('bp/<int:pk>/', BPEntryDetailView.as_view(), name='bpentry-detail'),
    path('bp/<int:pk>/update/', BPEntryUpdateView.as_view(), name='bpentry-update'),
    path('bp/<int:pk>/delete/', BPEntryDeleteView.as_view(), name='bpentry-delete'),
]