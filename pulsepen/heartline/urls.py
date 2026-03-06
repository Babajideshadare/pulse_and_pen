from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register,
    profile,
    BPEntryListView,
    BPEntryDetailView, 
    BPEntryCreateView,
    BPEntryUpdateView,
    BPEntryDeleteView,
    JournalEntryListView,
    JournalEntryCreateView,
    JournalEntryDeleteView,
    JournalEntryDetailView,
    JournalEntryUpdateView,
    DashboardView
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='heartline/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='heartline/logout.html'), name='logout'),
    path('register/', register, name ='register'),
    path('profile/', profile, name='profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('bp/', BPEntryListView.as_view(), name='bpentry-list'),
    path('bp/new/', BPEntryCreateView.as_view(), name='bpentry-create'),
    path('bp/<int:pk>/', BPEntryDetailView.as_view(), name='bpentry-detail'),
    path('bp/<int:pk>/update/', BPEntryUpdateView.as_view(), name='bpentry-update'),
    path('bp/<int:pk>/delete/', BPEntryDeleteView.as_view(), name='bpentry-delete'),

    path('journal/', JournalEntryListView.as_view(), name='journalentry-list'),
    path('journal/new/', JournalEntryCreateView.as_view(), name='journalentry-create'),
    path('journal/<int:pk>/', JournalEntryDetailView.as_view(), name='journalentry-detail'),
    path('journal/<int:pk>/update/', JournalEntryUpdateView.as_view(), name='journalentry-update'),
    path('journal/<int:pk>/delete/', JournalEntryDeleteView.as_view(), name='journalentry-delete'),
]