#获取标签名称
import urllib.request
import re
from urllib.parse import quote


url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
html = res.read().decode('utf8')
log = re.findall('<a href="/tag/.*?">(.*?)</a>', html, re.S)
print(log)
def get_log(n):
    log1 = quote(log[n])
    return log1
