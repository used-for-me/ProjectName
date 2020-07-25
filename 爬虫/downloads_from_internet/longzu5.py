import time
import urllib.error
import urllib.request
import chardet
from bs4 import BeautifulSoup
from 爬虫.downloads_from_internet import SMTP2


def download(url, user_agent='wswp', num_retries=2):
    """
    Good day is it today    """

    print('Downloading:', url)
    headers = {'user-agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries - 1)
    return html


def find_long_zu(url):
    get_html = download(url)
    get_html = get_html.decode(chardet.detect(get_html)['encoding'], 'ignore')
    soup = BeautifulSoup(get_html, "html.parser")
    # fixed_html = soup.prettify()
    # print('完善html')
    # soup = BeautifulSoup(fixed_html, "html.parser")
    my__html = []
    print("打开ile_long_zu.txt")
    with open("file_long_zu.txt", 'r') as fp:
        for line in fp:
            my__html.append(line)
    with open('bb.txt', 'w') as fp:
        fp.write(get_html)
    get__html = []
    for i in soup.find_all('dd'):
        if i.a:
            if (i.a.attrs['href'] + ' ' + i.a.string + '\n') not in my__html:
                print('i.a')
                print(i.a.attrs['href'])
                flag = download_long_zu('http://www.duoben.net' + i.a.attrs['href'])
                print('i.b')
                print(i.a.string)
                if flag:
                    get__html.append(str(i.a.attrs['href'] + ' ' + i.a.string))
                print(get__html, '111')
    print('写入file_long_zu.txt')
    if get__html:
        with open("file_long_zu.txt", 'a') as fp:
            for a_html in get__html:
                print(a_html)
                fp.write(str(a_html) + '\n')


def download_long_zu(url):
    get_html = download(url)
    get_html = get_html.decode(chardet.detect(get_html)['encoding'], 'ignore')
    soup = BeautifulSoup(get_html, "html.parser")
    fixed_html = soup.prettify()
    soup = BeautifulSoup(fixed_html, "html.parser")
    ss = soup.find('div', class_="showtxt", id="content", )
    # with open('bb.txt', 'w') as fp:
    #     fp.write(str(ss))
    print(ss)
    cc = soup.h1.string
    print(cc)
    # flag = SMTP2.sent_email(cc, ss)
    flag = 0
    if 0 < flag:
        return False
    else:
        return True


if __name__ == '__main__':
    find_long_zu('http://www.duoben.net/')
    # download_long_zu('http://www.duoben.net/book/11893/25983855.html')
    # f = ''.lower()

