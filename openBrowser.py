import webbrowser
from animechan import js
link = 'https://myanimelist.net/search/all?q=' + js['anime'] +'&cat=all'


def search_anime():
    webbrowser.open(link, new=2)
