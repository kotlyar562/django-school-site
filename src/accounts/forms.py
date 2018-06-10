from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from nocaptcha_recaptcha.fields import NoReCaptchaField

from . models import User

class AdminUserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class AdminUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'


class UserEditForm(forms.ModelForm):
    current_password = forms.CharField(label='Текущий пароль', widget=forms.PasswordInput, required=False,
                                       help_text='Введите Ваш текущий пароль, чтобы его изменить')
    current_password.widget.attrs.update({'autocomplit': 'off'})
    new_password = forms.CharField(label='Новый пароль', widget=forms.PasswordInput, required=False)
    new_password_verify = forms.CharField(label='Повторите новый пароль', widget=forms.PasswordInput,
                                          required=False)

    class Meta:
        model = User
        fields = ('photo', 'first_name', 'last_name', 'email', 'post', 'stag',
                  'rank', 'statement')

    def clean(self):
        current, new, verify = map(self.cleaned_data.get,
                                   ('current_password', 'new_password', 'new_password_verify'))
        if current and self.instance.has_usable_password() and not self.instance.check_password(current):
            raise forms.ValidationError('Неправильный пароль')
        if new and new != verify:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def clean_email(self):
        value = self.cleaned_data['email']
        if value:
            try:
                User.objects.exclude(pk=self.instance.pk).get(email=value)
                raise forms.ValidationError('Этот адрес электронной почты уже используется')
            except User.DoesNotExist:
                pass
        return value

    def save(self, commit=True):
        password = self.cleaned_data.get('new_password')
        if password:
            self.instance.set_password(password)
        return super(UserEditForm, self).save(commit)


class LoginUser (AuthenticationForm):
    captcha = NoReCaptchaField(label='Каптча')
