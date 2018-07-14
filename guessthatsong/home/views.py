from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
import urllib.request
import os

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

def create_replacement_dict(data):
    replacement_dict = {}
    lines = data.split("\n")
    for line in lines[2:-1]:
        if len(line.split(":")) == 3:
            word, emoji, _ = line.split(":")
            replacement_dict[word] = emoji
    return replacement_dict

def replace_words_with_mappings(song_html, mappings):
    print("Cleaning html")
    song_html = song_html.replace("<br>", " <br> ")
    song_html = song_html.replace("\n", "")
    song_html = song_html.replace(".", "")
    words = song_html.split(" ")
    replaced_song = ""
    print("Replacing words")
    for word in words:
        if word.lower() in mappings: replaced_song += " " + mappings[word.lower()]
        else:
            replaced_song += " " + word
    return replaced_song

class HomeView(TemplateView):
    template_name = "home.html"
    emoji_mappings_url = os.path.join('files/emoji_mappings.txt')
    emoji_mappings_wrapper = open(emoji_mappings_url, "r")
    emoji_mappings_raw = emoji_mappings_wrapper.read()
    emoji_mappings = create_replacement_dict(emoji_mappings_raw)

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
        song_html_raw = get_song_html(artist, song).decode('UTF-8')
        song_html = replace_words_with_mappings(song_html_raw, self.emoji_mappings)
        context = {"song_html": song_html}
        print("Context sent to song_display.html")
        return render(request, "song_display.html", context)
