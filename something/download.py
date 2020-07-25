import urllib.error
import urllib.request
import re



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

def start(url, html):
    html = str(html)
    html = html.lower()
    html = html.replace('\\n','')
    with open('my_lower.html','w') as fp:
        fp.write(html)

if __name__ == '__main__':
    url = 'https://redis.io/commands'
    start(url, download(url))
	
