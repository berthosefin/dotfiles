from pytube import YouTube
from sys import argv


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = int(bytes_downloaded * 100 / stream.filesize)
    print(f"Progression: {percent}%")


yt = YouTube(argv[1])
yt.register_on_progress_callback(on_download_progress)
print(f"Téléchargement {yt.title}")
stream = yt.streams.get_highest_resolution()
print("Fin du téléchargement.")

