# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm

def url_shorten_view(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            shortened_url = request.build_absolute_uri('/') + url.token
            return render(request, 'url_shorten.html', {'shortened_url': shortened_url, 'form': form})
    else:
        form = URLForm()
    return render(request, 'url_shorten.html', {'form': form})

def redirect_view(request, token):
    url = get_object_or_404(URL, token=token)
    return redirect(url.original_url)