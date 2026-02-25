from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import BPEntry

class BPEntryListVeiw(ListView):
    model = BPEntry
    template_name = 'heartline/bpentries_list.html'
    context_object_name = 'bpentries'
    ordering = ('-date', '-time')

class BPEntryDetailView(DetailView):
    model = BPEntry
    template_name = 'heartline/bpentries_detail.html'

class BPEntryCreateView(CreateView):
    model = BPEntry
    fields = ('date', 'time', 'systolic', 'diastolic', 'pulse', 'note')
    template_name = 'heartline/bpentries_create.html'
    success_url = reverse_lazy(BPEntryListVeiw)

class BPEntryUpdateView(UpdateView):
    model = BPEntry
    fields = ('date', 'time', 'systolic', 'diastolic', 'pulse', 'note')
    template_name = 'heartline/bpentries_update.html'
    success_url = reverse_lazy(BPEntryListVeiw)

class BPEntryDeleteView(DeleteView):
    model = BPEntry
    template_name = 'heartline/bpentries_confirm_delete.html'
    success_url = reverse_lazy(BPEntryListVeiw)