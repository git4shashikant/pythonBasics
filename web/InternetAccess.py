import urllib.request
import json
from html.parser import HTMLParser

web_url = urllib.request.urlopen("http://www.google.com")
print(web_url.getCode())
print(web_url.read())

jsonData = json.loads(web_url.read())
if "title" in jsonData["metadata"]:
    print(jsonData["metadata"]["title"])


class My_html_parser(HTMLParser):
