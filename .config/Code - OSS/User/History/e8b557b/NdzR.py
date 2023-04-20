from pytube import YouTube
from sys import argv


yt = YouTube(argv[1])
print(f"Téléchargement {yt.title}")
print("...")
