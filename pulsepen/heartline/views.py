from django.contrib.auth.mixins import LoginRequiredMixin

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


class BPEntryListView(LoginRequiredMixin, ListView):
    model = BPEntry
    template_name = 'heartline/bpentry_list.html'
    context_object_name = 'bp_entries'
    ordering = ('-date', '-time')
    login_url = 'login'

    def get_queryset(self):
        return BPEntry.objects.filter(user=self.request.user).order_by('-date', '-time')



class BPEntryDetailView(LoginRequiredMixin, DetailView):
    model = BPEntry
    template_name = 'heartline/bpentry_detail.html'
    login_url = 'login'

    def get_queryset(self):
        return BPEntry.objects.filter(user=self.request.user)

class BPEntryCreateView(LoginRequiredMixin, CreateView):
    model = BPEntry
    fields = ('date', 'time', 'systolic', 'diastolic', 'pulse', 'note')
    template_name = 'heartline/bpentry_form.html'
    success_url = reverse_lazy('bpentry-list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BPEntryUpdateView(LoginRequiredMixin, UpdateView):
    model = BPEntry
    fields = ('date', 'time', 'systolic', 'diastolic', 'pulse', 'note')
    template_name = 'heartline/bpentry_form.html'
    success_url = reverse_lazy('bpentry-list')
    login_url = 'login'

    def get_queryset(self):
        return BPEntry.objects.filter(user=self.request.user)

class BPEntryDeleteView(LoginRequiredMixin, DeleteView):
    model = BPEntry
    template_name = 'heartline/bpentry_confirm_delete.html'
    success_url = reverse_lazy('bpentry-list')
    login_url = 'login'

    def get_queryset(self):
        return BPEntry.objects.filter(user=self.request.user)