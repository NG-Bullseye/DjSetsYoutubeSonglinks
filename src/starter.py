import os.path
import sys
import yaml
import scripts.ytdpl as ytdpl
if __name__ == "__main__":
    sys.path.insert(1,os.path.abspath('.'))
    class PrettySafeLoader(yaml.SafeLoader):
        def construct_python_tuple(self, node):
            return tuple(self.construct_sequence(node))
    PrettySafeLoader.add_constructor(
        u'tag:yaml.org,2002:python/tuple', PrettySafeLoader.construct_python_tuple)
    current_directory = os.getcwd()
    print("Program directory:", current_directory)
    with open('changeMe.yaml', 'r') as stream:
        params = yaml.load(stream, Loader=PrettySafeLoader)
    playlist_dir = params['DOWNLOAD_DIR']
    playlist_name = params['PLAYLIST_FILE_NAME']
    playlist_url = params['YOUTUBE_PLAYLIST_LINK']
    ytdpl.download_playlist_as_flac(playlist_name, playlist_url,playlist_dir)
