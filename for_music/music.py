import urllib.request
import urllib.error
# import urllib.robotparser
import re


def download(url, user_agent='wswp', num_retries=2):
    print('downloading:', url)
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        print('Dowmload error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # is 5xx HTTP errors
                return download(url, user_agent, num_retries - 1)
    return html


def link_crawler(seed_url, link_regex):
    craw_queue = [seed_url]
    while craw_queue:
        url = craw_queue.pop()
        html = download(url)
        for link in getlinks(html):
            if re.match(link_regex, link):
                link=link if re.match('^http', link) else html

                craw_queue.append(link)


def getlinks(html):
    """

    :param html:
    :return: return a list of links from html
    """
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)
