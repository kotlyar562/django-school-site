from django.shortcuts import get_object_or_404, render

from . models import Page

def page(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    return render(request, 'pages/page.html', {'page': page})
