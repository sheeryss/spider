#将邮箱中获取的命令转入数据库
import pymysql
from send_mail import send_mes

conn = pymysql.connect('localhost', 'root', '666666', 'test', charset='utf8')
cursor = conn.cursor()
def mysql_fx(order, sender):

    sql = """select name,score from books where author='%s'""" % order
    cursor.execute(sql)
    all = cursor.fetchall()
    print(all)
    i = 0
    all2 = ''
    while True:
        try:
            all1 = "".join(tuple(all[i]))
            all2 = all2 + all1 + '\n'
            i += 1
        except:
            break
    send_mes(all2, sender)

