# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#django.shortcuts import render
from django.http import HttpResponse

#from .models import ALBUMS

# Create your views here.
def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)

def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)

def detail(request, album_id):
    id = int(album_id)
    album = ALBUMS[id]
    artists = " ".join([artist['name'] for artist in album['artists']])
    message = "LE nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)

def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun artiste n'est demandé"
    else:
        albums = [
            album for album in ALBUMS
            if query in " ".join(artist['name'] for artist in album['artists'])
        ]

        if len(albums) == 0:
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = ["<li>{}</li>".format(album['name']) for album in albums]
            message = """
                nous avons trouvé les albumes correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(albums))

    return HttpResponse(message)