#import pandas as pd
import pymysql
import csv

conn = pymysql.connect('localhost', 'root', '666666', 'test', charset='utf8')
cursor = conn.cursor()
sqlcmd = "select * from books"
cursor.execute(sqlcmd)
all = cursor.fetchall()
all2 = []
i = 0
while True:
    try:
        all1 = []
        all1 = list(all[i])
        #print(all1)
        all2.append(all1)
        i += 1
    except:
        break
print(all2)
print('start')
with open('D:\\Pythontest\\py_mysql\\12.csv', 'w+', newline='', encoding='utf8') as fp:
    #print('start1')
    a = csv.writer(fp,delimiter=',')
    #print('start2')
    a.writerow(['编  号','书  名','作  者','评  分','评价人数'])
    #print('start3')
    a.writerows(all3)
        #print('保存完毕')
#except:
    #print('fail')
#print(all)
#except:
    #print("fail")
cursor.close()
conn.close()
