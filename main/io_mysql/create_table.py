#在数据库中建表以保存图书信息
import pymysql

conn = pymysql.connect('localhost', 'root', '666666', 'test')

cursor = conn.cursor()

sql = """create table books(id int  primary key auto_increment, name VARCHAR(100),author VARCHAR(100), score varchar(50), arg varchar(50))"""

cursor.execute(sql)

conn.commit()
conn.close()
