from django.shortcuts import render, redirect
from .models import Song

# Create your views here.

def index(request):
    songs = Song.objects.all()
    context = {'songs': songs}
    return render(request, 'crud/index.html', context)

def create(request):
    song = Song(title=request.POST['title'], artist=request.POST['artist'])
    song.save()
    return redirect('/')

def edit(request, id):
    songs = Song.objects.get(id=id)
    context = {'songs': songs}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    song = Song.objects.get(id=id)
    song.title = request.POST['title']
    song.artist = request.POST['artist']
    song.save()
    return redirect('/crud/')

def delete(request, id):
    song = Song.objects.get(id=id)
    song.delete()
    return redirect('/crud/')