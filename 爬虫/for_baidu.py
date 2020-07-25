import urllib.request
import urllib.error
myurl = 'http://www.baidu.com/s'
keyword = 'python'


def download(url, user_agent='wswp', num_retries=2):
    print('downloading:', url)
    header = {'user-agent': user_agent}
    requests = urllib.request.Request(url, header)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        print('url error :', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <= 600:
                return download(url, user_agent, num_retries - 1)
    return html


myhtml = download(myurl).decode().splitlines()
print(myhtml)
with open('html', 'w') as fp:
    for hh in myhtml:
        if hh != '':
            fp.writelines(hh)
        else:
            print('k+', hh)
            # print(hh)
