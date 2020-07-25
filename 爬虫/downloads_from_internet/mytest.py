from urllib import request
import urllib.error
import chardet
from urllib import response
from bs4 import BeautifulSoup


def download(url, user_agent='asgn', num_retries=2):
    print('DownLoading:' + url)
    headers = {'user-agent': user_agent}
    requests = request.Request(url=url, headers=headers)
    try:
        html = request.urlopen(url=url).read()
        print(html)
    except urllib.error.URLError as e:
        print('download error.' + e.reason)
        if num_retries > 0:
            if hasattr(e, 'code') and 500 < e.code < 600:
                return download(url, user_agent, num_retries - 1)
    return html


def get_html(html):
    html = html.decode(chardet.detect(html)['encoding'], 'ignore')
    return html


if __name__ == '__main__':
    html1 = download('http://www.duoben.net/book/11893/25983855.html')
    with open('bb.txt', 'w+')as fp:
        fp.write()

