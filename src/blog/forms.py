from django import forms
from redactor.widgets import RedactorEditor

from . models import Article


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')
        widgets = {
            'content': RedactorEditor(),
        }

    def save(self, commit=False):
        return super(AddArticleForm, self).save(commit)


class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')
        widgets = {
            'content': RedactorEditor(),
        }

    def save(self, commit=True):
        return super(EditArticleForm, self).save(commit)
