import json
import urllib.request
import string
import random

count = 50
API_KEY = 'AIzaSyBfCIH48MrcQAF-GZSCXblJBiMxoHg_np4'
random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,random)
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
results = json.loads(data.decode(encoding))
video_ids = []
for data in results['items']:
    videoId = (data['id']['videoId'])
    # print(videoId)
    video_ids.append(videoId)

# print(video_ids)
    #store your ids
new_links = []
for i in video_ids:
    leenk = "https://www.youtube.com/watch?v=" + i
    new_links.append(leenk)

# print(new_links)
for i in new_links:
    i = str(i)
    f = open("links2.csv", "a")
    f.write(f'{i}\n')
    f.close()