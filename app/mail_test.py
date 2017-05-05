# -*- coding: UTF-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask,render_template
from flask.ext.mail import Mail,Message
from threading import Thread

app = Flask(__name__)
#下面是SMTP服务器配置
app.config['MAIL_SERVER'] = 'smtp.googlemail.com' #电子邮件服务器的主机名或IP地址
app.config['MAIL_PORT'] = '587' #电子邮件服务器的端口
app.config['MAIL_USE_TLS'] = True #启用传输层安全
#app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') #邮件账户用户名
#app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') #邮件账户的密码
app.config['MAIL_USERNAME'] = 'ypypatricka@gmail.com' #邮件账户用户名
app.config['MAIL_PASSWORD'] = 'Patricka06_06' #邮件账户的密码
mail = Mail(app)


def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

@app.route('/')
def index():
    msg = Message('这是题目',sender='ypypatricka@gmail.com', recipients=['277079165@qq.com'])
    msg.body = '文本 body'
    msg.html = '<b>这是HTML测试</b> body'
    #mail.send(msg)

    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()

    return '<h1>邮件发送成功</h1>'

if __name__ == '__main__':
    app.run(debug=True)