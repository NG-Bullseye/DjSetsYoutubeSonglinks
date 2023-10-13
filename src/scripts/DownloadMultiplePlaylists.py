from playlistToUrlList import main as gerUrlFile
from downloader import main as startdownload
import json


with open('playlists.json', 'r') as f:
    distros_dict = json.load(f)

from downloader import main as download
from playlistToUrlList import main as toSongUrlList

for distro in distros_dict:
    print(distro['Name'])
    print(distro['URL'])
    toSongUrlList(distro['Name'],distro['URL'])
    download(distro['Name'])