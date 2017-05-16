from __future__ import unicode_literals
import youtube_dl
from tkinter import *


import os
music_path = "T:/Music"
options = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': 'mp3',
    'outtmpl': music_path + '\%(title)s' + ".mp3"
}

def get_info(url):
    info = []
    with youtube_dl.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=False)
    for data in info:
        print(data)

def download_song(url, playlist):
    options['noplaylist'] = not playlist
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])

