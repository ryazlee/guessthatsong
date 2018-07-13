from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
import urllib.request

# Variables
song_url_base = "http://www.azlyrics.com/lyrics/#FILLIN#.html"

# Helper functions

def get_song_html(artist, song):
    song_url = song_url_base.replace("#FILLIN#", artist + "/" + song)
    print("Getting html from", song_url)
    response = urllib.request.urlopen(song_url)
    song_raw_html = response.read()
    song_html = get_song_from_raw_html(song_raw_html)
    return song_html

def get_song_from_raw_html(raw_html):
    song_start = raw_html.index("<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->".encode()) + 133
    song_end = raw_html.index("<!-- MxM banner -->".encode()) - 14
    song_html = raw_html[song_start:song_end]
    return song_html

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        """
        Load context data for home page
        """
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):
        """
        Define post function of web page
        """
        song = request.POST["song"]
        artist = request.POST["artist"]
        song_html = get_song_html(artist, song)
        context = {"song_html": song_html}
        return render(request, "song_display.html", context)
