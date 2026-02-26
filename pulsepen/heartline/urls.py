from django.urls import path
from .views import (
    BPEntryListView,
    BPEntryDetailView, 
    BPEntryCreateView,
    BPEntryUpdateView,
    BPEntryDeleteView,
)

urlpatterns = [
    path('bp/', BPEntryListView.as_view(), name='bpentry-list'),
    path('bp/new/', BPEntryCreateView.as_view(), name='bpentry-create'),
    path('bp/<int:pk>/', BPEntryDetailView.as_view(), name='bpentry-detail'),
    path('bp/<int:pk>/update/', BPEntryUpdateView.as_view(), name='bpentry-update'),
    path('bp/<int:pk>/delete/', BPEntryDeleteView.as_view(), name='bpentry-delete'),
]