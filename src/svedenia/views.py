from django.shortcuts import render, get_object_or_404
from . models import Group


def index(request):
    groups = Group.objects.all()
    return render(request, 'svedenia/index.html', {'groups': groups})


def group_view(request, group_slug):
    groups = Group.objects.all()
    group = get_object_or_404(Group, slug=group_slug)
    return render(request, 'svedenia/group.html', {'group': group, 'groups': groups})
