"""
就像我们可以用HTTP（超文本传输协议）来访问一个网站一样，发送邮件要使用SMTP（简单邮件传输协议），SMTP也是一个建
立在TCP（传输控制协议）提供的可靠数据传输服务的基础上的应用级协议，它规定了邮件的发送者如何跟发送邮件的服务器进行
通信的细节，而Python中的smtplib模块将这些操作简化成了几个简单的函数
"""

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'kobe@qq.com'
    receivers = ['tracyxx@gmail.com','make@163.com']
    message = MIMEText('这是我的第一个Python邮件程序.', 'plain', 'utf-8')
    message['From'] = Header('kobe','utf-8')
    message['to'] = Header('tracy','utf-8')
    message['subject'] = Header('old brother stable','utf-8')
    smtper = SMTP('smtp.qq.com')
    smtper.login(sender,'me123456')
    smtper.sendmail(sender,receivers,message.as_string())
    print('发送邮件成功')


if __name__ == '__main__':
    main()