# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#django.shortcuts import render
from django.http import HttpResponse

from .models import Album, Artist, Contact, Booking

# Create your views here.
def index(request):
    albums = ["<li>{}</li>".format(album.title) for album in Album.objects.filter(available=True).order_by('-created_at')[:5]]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)

def listing(request):
    albums = ["<li>{}</li>".format(album.title) for album in Album.objects.filter(available=True).order_by('-created_at')]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)

def detail(request, album_id):
    id = int(album_id)
    album = Album.objects.get(pk=id)
    artists = " ".join([artist.name for artist in album.artists.all()])
    message = "LE nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
    return HttpResponse(message)

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)

    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)

    if not albums.exists():
        message = "Misère de misère, nous n'avons trouvé aucun résultat !"
    else:
        albums = ["<li>{}</li>".format(album.title) for album in albums]
        message = """
            Nous avons trouvé les albums correspondant à votre requête ! Les voici :
            <ul>{}</ul>
        """.format("</li><li>".join(albums))

    return HttpResponse(message)