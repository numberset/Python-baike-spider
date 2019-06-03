# 百度百科Python爬虫实例
# https://www.imooc.com/learn/563
# https://github.com/lovefengruoqing/baike_spider

import urllib.request

class HtmlDownloader(object):


    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()


    