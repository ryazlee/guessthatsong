from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
import urllib.request as urllib2

# Helper functions

def get_song_html(artist, song):
    response = urllib2.urlopen('http://python.org/')
    html = response.read()
    print(html)


class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        """
        Load context data for home page
        """
        context = super().get_context_data(**kwargs)
        context['song_html'] = 'workfromhome'
        return context
    
    def post(self, request):
        """
        Define post function of web page
        """
        song = request.POST["song"]
        artist = request.POST["artist"]
        get_song_html(artist, song)
        return render(request, "home.html")
