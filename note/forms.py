from django import forms
from .models import Note


class Note_Form(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Title', 'cols': 1, 'rows': 1}),
                            label='')
    context = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Content'}), label='', required=False)

    class Meta:
        model = Note
        ordering = ('title',)
        fields = ('title', 'context')
