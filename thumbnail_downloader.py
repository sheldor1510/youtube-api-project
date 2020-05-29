import json
import re
import urllib.request
import os
try:
    os.remove("links.txt")
except:
    pass
youtuber = input('Write the name of the youtuber:')
os.mkdir(youtuber) 
print()
channel_id_here = input("Channel ID =")
<<<<<<< HEAD
api_key = "AIzaSyCingHnG2DYG3IjMRPq52YueO95dpUtoUM"
urlData =  f"https://www.googleapis.com/youtube/v3/search?part=id%2Csnippet&maxResults=100&channelId={channel_id_here}&key={api_key}"
=======

>>>>>>> 15a88a1a0e1d984deba6b0f23078d884a3162e03
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
results = json.loads(data.decode(encoding))
video_ids = []
try:
    for data in results['items']:
        videoId = (data['id']['videoId'])
        # print(videoId)
        video_ids.append(videoId)
except:
    pass

new_links = []
for i in video_ids:
    leenk = "https://www.youtube.com/watch?v=" + i
    new_links.append(leenk)

# print(new_links)
for i in new_links:
    i = str(i)
    f = open("links.txt", "a")
    f.write(f'{i}\n')
    f.close()

class Helper():
    def __init__(self):
        pass

    def title_to_underscore_title(self, title:str):
        title = re.sub('[\W_]+', "_", title)
        return title.lower()

    def id_from_url(self, url:str):
        return url.rsplit("=", 1)[1]


class YouTubeStats:
    def __init__(self, url:str):
        self.json_url = urllib.request.urlopen(url)
        self.data = json.loads(self.json_url.read())

    def print_data(self):
        print(self.data)

    def get_video_title(self):
        return self.data["items"][0]["snippet"]["title"]

    def get_video_description(self):
        return self.data["items"][0]["snippet"]["description"]

    def get_video_thumbnail(self):
        return self.data["items"][0]["snippet"]["thumbnails"]["default"]["url"]



# api_key = "AIzaSyBfCIH48MrcQAF-GZSCXblJBiMxoHg_np4"
text_file = open("links.txt", "r")
content = text_file.readlines()
content = list(map(lambda s: s.strip(), content))
i = 0
helper = Helper()
for youtube_url in content:
    video_id = helper.id_from_url(youtube_url)
    url =  f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
    yt_stats = YouTubeStats(url)
    title = yt_stats.get_video_title()
    title = helper.title_to_underscore_title(title)

    description = yt_stats.get_video_description()
    thumbnail = yt_stats.get_video_thumbnail()
    fullfilename = os.path.join(youtuber, "img_" + str(i) + ".png")
    urllib.request.urlretrieve(thumbnail, fullfilename)
    i += 1






