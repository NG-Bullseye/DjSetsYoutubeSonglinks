from boltons.setutils import IndexedSet
import subprocess

def main(name,url):
    data = subprocess.check_output(["youtube-dl", "--dump-json", "--flat-playlist", url]).decode("utf-8").replace("null", "None").split("\n")[:-1]
    url_list = IndexedSet(f"https://www.youtube.com/watch?v={eval(item)['id']}" for item in data)
    with open("url_file.txt", "w") as f:
        for url in url_list:
            print(url)
            f.writelines(url+"\n")
    with open(name+".txt", "w") as f:
        for url in url_list:
            print(url)
            f.writelines(url+"\n")

