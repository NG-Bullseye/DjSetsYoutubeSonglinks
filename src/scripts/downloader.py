import os

import youtube_dl
import subprocess
import os

def main(setName="new"):

    newpath = r'D:\DJ Tracks\DjSetsYoutubeSonglinks\src\Sets\\'+setName
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    opts = {
        'format': 'bestaudio/best',
        'outtmpl': r'D:\DJ Tracks\DjSetsYoutubeSonglinks\src\Sets\\'+setName+'\%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '320',
        }]
    }

    url_file = "./url_file.txt"

    with open(url_file, "r") as f:
        url_list = f.readlines()
        print(url_list)

    with youtube_dl.YoutubeDL(opts) as ydl:
        for url in url_list:
            try:
                ydl.download([url])
            except Exception as e:
                print(url, e)


if __name__ == '__main__':
    main()
