
import re

#模块用于从每页HTML中提取所需的内容，减少程序运行时间
def get_main(html):
    main = re.findall(r'<div class="info">(.*?)</li>', html, re.S)
    #print(len(main))
    return main
#获得书名
def get_bookname(main):
    #print (main)
    name = []
    for i in range(0,len(main)):
        name1 = re.findall(r'<a href=.*? title="(.*?)"', main[i], re.S)
        name.append(name1[0])
    #print(name)
    return name
#获得作者名
def get_author(main):
    author = []
    for i in range(0, len(main)):
        author1 = re.findall(r'<div class="pub">\n        \n  \n  (.*?) /.*?</div>', main[i], re.S)
        author.append(author1[0])
    #print(author)
    return author
#获得评分
def get_score(main):
    score = []
    for i in range(0, len(main)):
        score1 = re.findall(r'<span class="rating_nums">(.*?)</span>', main[i], re.S)
        if score1 == []:
            score1 = [0]
        score.append(score1[0])
    #print(score)
    return score
#获得评价人数
def get_number(main):
    number = []
    for i in range(0, len(main)):
        number1 = re.findall(r'<span class="pl">\n        [(](.*?)[)]\n    </span>', main[i], re.S)
        number.append(number1[0])
    #print(number)
    return number
