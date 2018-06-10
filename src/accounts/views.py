from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from . models import User
from . forms import UserEditForm

def index(request):
    return render(request, 'accounts/index.html',
                  {'teachers': User.objects.all()})


def profile(request, user_pk):
    return render(request, 'accounts/profile.html',
                  {'user_obj': get_object_or_404(User, pk=user_pk)})


@login_required()
def edit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно сохранен.')
            return redirect('accounts:profile', request.user.pk)
        messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'accounts/edit.html', {'form':form})


def logout(request):
    logout(request)
    return redirect('/')
