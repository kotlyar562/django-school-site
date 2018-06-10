from django import forms
from redactor.widgets import RedactorEditor

from . models import News


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'date_add')
        widgets = {
            'content': RedactorEditor(),
        }

    def save(self, commit=False):
        return super(AddNewsForm, self).save(commit)


class EditNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'tags', 'date_add')
        widgets = {
            'content': RedactorEditor(),
        }

    def save(self, commit=True):
        return super(EditNewsForm, self).save(commit)
