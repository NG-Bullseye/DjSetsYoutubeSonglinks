import json
import os
from yt_dlp import YoutubeDL
from boltons.setutils import IndexedSet
import subprocess


def download_playlist_as_flac(playlist_name, playlist_url,download_download_path):
    output_folder = os.path.join(download_download_path, playlist_name)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'flac'},
            {'key': 'FFmpegMetadata'},
        ],
    }



    data = subprocess.check_output(["yt-dlp", "--dump-json", "--flat-playlist", playlist_url]).decode("utf-8").replace(
        "null", "None").split("\n")[:-1]
    url_list = IndexedSet(f"https://youtu.be/{eval(item)['id']}" for item in data)

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url_list)