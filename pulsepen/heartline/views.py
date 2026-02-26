from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import BPEntry


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'heartline/register.html', {'form': form})


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