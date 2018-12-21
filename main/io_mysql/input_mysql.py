#将图书信息输入数据库
import pymysql

def input_ml(name, author, score, arg, num):
    conn = pymysql.connect('localhost', 'root', '666666', 'test', charset='utf8')
    cursor = conn.cursor()
    #print(name)
    for i in range(0, num):
        sql = """INSERT INTO books (name, author, score, arg)
                 VALUES ('%s', '%s', '%s', '%s')""" % (name[i], author[i], score[i], arg[i])
        try:
            #print('1s')
            cursor.execute(sql)
            conn.commit()
            #print('make it')
        except:
            conn.rollback()
            print('fail')

    conn.close()
