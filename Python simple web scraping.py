import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup
import re

# 网页下载器实例
url = "http://www.baidu.com"
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(len(response3.read()))
print(cj)



