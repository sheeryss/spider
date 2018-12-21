#获得不同标签页的网址和内容
import urllib.request
import random
from get_url import get_log
import time

#获得每页的url
def get_pageurl(i, n):
    log = get_log(n)
    #print('kaishi')
    url = "https://book.douban.com/tag/" + log
    page = i * 20
    last = '&type=T'
    first = '?start='
    page_url = url + first + str(page) + last
    return page_url
#获得每页的HTML
def get_html(page_url):
    time.sleep(3)
    list1 = ['120.241.0.52:80', '58.240.53.196:80', '182.141.42.79:9000']
    proxy_support = urllib.request.ProxyHandler({'http': random.choice(list1)}) #随机代理ip设置，避免单一ip过多访问服务器被拒绝

    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36')]#给代理ip加上通行证

    urllib.request.install_opener(opener)

    req = urllib.request.Request(page_url)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html
