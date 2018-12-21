#该模块主要用于获取豆瓣网站的图书信息
import csv
import time
from get_page_html import get_pageurl, get_html
from main.io_mysql.input_mysql import input_ml
from get_message import get_main, get_bookname, get_author, get_score, get_number

#主函数
n = 0
number = 1

while True:
    page = 0
    while True:
        page_url = get_pageurl(page, n)
        #初始化数据
        book_list = []
        author_list = []
        score_list = []
        number_list = []
        try:
            #print(page_url)
            html = get_html(page_url)
            #print(html)
            main = get_main(html)
            #print(main)
            if main == []:
                print('爬下一个标签')
                break
            book_list = get_bookname(main)
            author_list = get_author(main)
            score_list = get_score(main)
            number_list = get_number(main)
            #保存到数据库
            input_ml(book_list, author_list, score_list, number_list, len(main))
            page += 1
            time.sleep(1)
            print('第%d页' % page)
            if number % 3 == 0:
                print('休息一会儿')
                time.sleep(30)
            number += 1
        except:
            print('爬取异常')
            print('哦豁，被封了？')
            exit()
    n += 1
    if page_url == '':
        break

print("爬取结束")
print(time.ctime(time.time()))
