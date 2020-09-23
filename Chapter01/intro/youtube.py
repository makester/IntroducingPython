import json
from urllib.request import urlopen
url = "https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/youTube_top_rated.json"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:3]:
    print(video['title']['$t'])

print('type of responce:{}'.format(type(response)))
print('type of contents:{}'.format(type(contents)))
print('type of text:{}'.format(type(text)))
print('type of data:{}'.format(type(data)))
print(data)