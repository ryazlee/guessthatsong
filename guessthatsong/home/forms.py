from django import forms
    
class SongForm(forms.Form):
    artist = forms.CharField(help_text="DSAF")
    song = forms.CharField(help_text="SADFD SONG")
