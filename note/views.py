from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.urls import reverse_lazy
from .models import Note
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import NoteForm


class RegView(generic.CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        user = authenticate(self.request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)
        return redirect('note:list-note')


class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    template_name = 'note/add_up_note.html'
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return redirect('note:list-note')


# class NoteDetailView(LoginRequiredMixin, generic.DetailView):
#     login_url = reverse_lazy('login')
#     template_name = 'note/note_view.html'

#     def get_queryset(self):
#         return Note.objects.filter(pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['user_view'] = self.get_queryset()
#         return context


class NoteListView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login')
    model = Note
    template_name = 'note/list_note.html'
    context_object_name = 'note_list'
    queryset = Note.objects.order_by('-created_at')

    def get_queryset(self):
        if self.request.user.is_superuser: return Note.objects.all()
        return Note.objects.filter(owner=self.request.user)


class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'note/delete_note.html'
    model = Note
    context_object_name = 'note_delete'
    success_url = reverse_lazy('note:list-note')


class NoteUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    template_name = 'note/add_up_note.html'
    context_object_name = 'note'
    form_class = NoteForm
    model = Note
    success_url = reverse_lazy('note:list-note')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context
