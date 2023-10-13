from boltons.setutils import IndexedSet
import subprocess

def main():
    print("Enter Playlist Url")
    playlist = input()
    print("Enter Playlist Name")
    name=input()
    data = subprocess.check_output(["youtube-dl", "--dump-json", "--flat-playlist", playlist]).decode("utf-8").replace("null", "None").split("\n")[:-1]
    url_list = IndexedSet(f"https://www.youtube.com/watch?v={eval(item)['id']}" for item in data)
    with open("url_file.txt", "w") as f:
        for url in url_list:
            print(url)
            f.writelines(url+"\n")
    with open(name+".txt", "w") as f:
        for url in url_list:
            print(url)
            f.writelines(url+"\n")

    from downloader import main
    main(name)
if __name__ == '__main__':
    main()