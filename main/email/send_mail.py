#将数据库中搜索到的相关信息发送给客户
# coding: utf-8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

# 输入Email地址和口令:
from_addr = 'sheerys33@163.com'
password = 's1443394209'
# 输入SMTP服务器地址:
smtp_server = 'smtp.163.com'
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mes(mes, sender):
    if mes == '':
        mes1 = '豆瓣无此作者相关的图书'
    else:
        mes1 = "豆瓣网上该作者的书集及评分：\n" + mes
    msg = MIMEText(mes1, 'plain', 'utf-8')
    msg['From'] = _format_addr('勇哥哥 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % sender)
    msg['Subject'] = Header('测试程序中', 'utf-8').encode()

    try:
        #print("次数")
        server = smtplib.SMTP(smtp_server, 25)#SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [sender], msg.as_string())
        server.quit()
    except:
        print('fail')
