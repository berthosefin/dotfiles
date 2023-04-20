from pytube import YouTube
from sys import argv


yt = YouTube(argv[1])
print(f"Téléchargement {yt.title}")
stream = yt.streams.get_highest_resolution()
print("Fin du téléchargement.")

