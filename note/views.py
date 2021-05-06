from django.shortcuts import render, reverse, get_object_or_404
from django.urls import reverse_lazy
from .models import Note
from django.contrib import messages
from django.views import generic
from .forms import Note_Form


class Note_Create(generic.CreateView):
    template_name = 'note/note_form.html'
    form_class = Note_Form
    success_url = reverse_lazy('create')
    warning_message = ''
    success_message = 'Note is Successfully Created!'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        # return self.render_to_response(self.get_context_data(request=self.request, form=form))
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.POST.get('title'):
            self.warning_message = 'This Note Exists in the System!'
        else:
            self.warning_message = 'Note Title cannot be Empty!'
        messages.warning(self.request, self.warning_message)
        return super().form_invalid(form)


class Note_View(generic.DetailView):
    template_name = 'note/note_view.html'

    def get_queryset(self):
        return Note.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_view'] = self.get_queryset()
        return context


class Note_List(generic.ListView):
    model = Note
    template_name = 'note/note_list.html'
    context_object_name = 'note_list'
    queryset = Note.objects.order_by('-created_at')


class Note_Delete(generic.DeleteView):
    template_name = 'note/delete_confirmation.html'
    model = Note
    context_object_name = 'note_delete'
    success_url = reverse_lazy('view')


class Note_Update(generic.UpdateView):
    template_name = 'note/note_form.html'
    context_object_name = 'note_update'
    form_class = Note_Form
    warning_message = 'This Note Title is in Used!'
    success_message = 'Note is Successfully Updated!'
    model = Note

    def form_valid(self, form):
        title_update = form.cleaned_data['title']
        dup_title = Note.objects.filter(title=self.request.POST.get('title'))
        if title_update != self.kwargs['pk'] and dup_title:
            messages.warning(self.request, self.warning_message)
            return super().form_invalid(form)

        if self.kwargs['pk'] != title_update:
            Note.objects.filter(pk=self.kwargs['pk']).delete()
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

# class Note_Delete(generic.DeleteView):
#     model = Note
#     template_name = 'note/note_list.html'

# def add_edit_note(request):
#     note_id = int(request.GET.get('note_id', 0))
#     note_attribute = Document.objects.all()
#     if request.method == 'POST':
#         note_id = int(request.POST.get('note_id', 0))
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         # to fetch and check if note title exists or not
#         note_title = Document.objects.filter(title=title)
#         if note_title and note_id <= 0:
#             messages.warning(request, 'This Note Title is in Used!')
#             return render(request, 'note_list.html', {'note_attribute': note_attribute, 'note_id': 0, 'invalid': 'Invalid'})
#         if title == '':
#             messages.warning(request, 'Note Title can not be Empty!')
#             return render(request, 'note_list.html', {'note_attribute': note_attribute, 'note_id': 0, 'invalid': 'Invalid'})
#         # to handle updates
#         if note_id > 0:
#             document = Document.objects.get(pk=note_id)
#             document.title = title
#             document.content = content
#             document.save()
#             messages.success(request, 'The Note was Successfully Updated!')
#             return redirect('/?note_id=%i' % note_id)
#         else:
#             document = Document.objects.create(title=title, content=content)
#             messages.success(request, 'The Note was Successfully Created!')
#             return redirect('/?note_id=%i' % document.id)
#     if note_id > 0:
#         document = Document.objects.get(pk=note_id)
#     else:
#         document = ''
#     note = {
#         'note_id': note_id,
#         'note_attribute': note_attribute,
#         'document': document
#     }
#     return render(request, 'note_list.html', note)

# delete object in manual method
# def delete_note(request, title):
#     document = Note.objects.get(title=title)
#     document.delete()
#     return redirect('/')
