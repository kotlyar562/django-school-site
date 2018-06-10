from django import forms
from django.core.mail import EmailMessage
from django.utils import timezone
from nocaptcha_recaptcha.fields import NoReCaptchaField


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Представьтесь', required=False ,widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    email = forms.EmailField(label='Email', required=False, widget=forms.TextInput(attrs={'placeholder': 'Электронный адрес'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(), required=True)
    captcha = NoReCaptchaField(label='Каптча')

    def send(self, request):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = '%s\n\nОтправитель: %s' % (message, name,)
        headers = {'Reply-To': email} if email else None
        EmailMessage('Письмо с сайта школы', message, email, ['feoschool7@yandex.ru',], headers=headers).send()


class FeedbackErrorForm(forms.Form):
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(), required=True)
    referer = forms.CharField(required=False, widget=forms.HiddenInput())
    captcha = NoReCaptchaField(label='Каптча')

    def send(self, request):
        message = self.cleaned_data['message']
        user_agent_data = 'User agent: %s' % request.META.get('HTTP_USER_AGENT')
        timestamp = 'Time: %s' % timezone.now().strftime('%H:%M:%S %m-%d-%Y')
        referer = 'Referer: %s' % self.cleaned_data['referer']
        message = '%s\n\n%s\n%s\n%s' % (message, user_agent_data, timestamp, referer)
        EmailMessage('Письмо с сайта школы!', message, None, ['kotlyar562@gmail.com',], headers=None).send()
