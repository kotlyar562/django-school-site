from django import forms
from redactor.widgets import RedactorEditor
from . models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields =('title', 'etype', 'klass', 'date_begin', 'date_end', 'content')
        widgets = {
            'content': RedactorEditor(),
        }

    def save(self, commit=True):
        return super(EventForm, self).save(commit)
