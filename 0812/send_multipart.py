#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('Form: ')
password = input('Password: ')
to_addr = input('To:')
smtp_server = input('SMTP server: ')

# 邮件对象 
msg = MIMEMultipart()
msg['From'] = _format_addr('Python Biao Ge<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候.....', 'utf-8').encode()

# 邮件正文是是:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件是加上一个MIMEBase，从本地读取图片:
with open('./meal.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型
    mime = MIMEBase('image', 'jpg', filename='meal.jpg')

    #加上必要的信息
    mime.add_header('Content-Disposition', 'attachment', filename='meal.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')

    # 把附件的内容读进来
    mime.set_payload(f.read())

    # 用Base64编码
    encoders.encode_base64(mime)

    # 添加到MIMEMultipart:
    msg.attach(mime)


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
