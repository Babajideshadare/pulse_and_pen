from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import BPEntry

class BPEntryListView(ListView):
    model = BPEntry
    template_name = 'heartline/bpentry_list.html'
    context_object_name = 'bp_entries'
    ordering = ('-date', '-time')

class BPEntryDetailView(DetailView):
    model = BPEntry
    template_name = 'heartline/bpentry_detail.html'

class BPEntryCreateView(CreateView):
    model = BPEntry
    fields = ('date', 'time', 'systolic', 'diastolic', 'pulse', 'note')
    template_name = 'heartline/bpentry_form.html'
    success_url = reverse_lazy('bpentry-list')

class BPEntryUpdateView(UpdateView):
    model = BPEntry
    fields = ('date', 'time', 'systolic', 'diastolic', 'pulse', 'note')
    template_name = 'heartline/bpentry_form.html'
    success_url = reverse_lazy('bpentry-list')

class BPEntryDeleteView(DeleteView):
    model = BPEntry
    template_name = 'heartline/bpentry_confirm_delete.html'
    success_url = reverse_lazy('bpentry-list')