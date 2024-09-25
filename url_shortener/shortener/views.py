from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm

def shorten_url(request):
    form = URLForm(request.POST or None)
    short_url = None

    if request.method == 'POST' and form.is_valid():
        url_instance = form.save()
        short_url = request.build_absolute_uri('/') + url_instance.short_code

    return render(request, 'shortener/index.html', {'form': form, 'short_url': short_url})

def redirect_url(request, short_code):
    url_instance = get_object_or_404(URL, short_code=short_code)
    return redirect(url_instance.original_url)
