import smtplib
from email.mime.text import MIMEText
from email.header import Header

#第三方smtp服务

mail_host = "smtp.qq.com"
mail_user = "XXXXXXX"
mail_pass = "XXXXXXX"

sender = 'XXXXXX@qq.com'
receiver = ['XXXXX@gmail.com']

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("this is from header",'utf-8')
message['To'] = Header('this is to header','utf-8')

subject = 'python smtp test'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25) #25为smtp端口
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receiver,message.as_string())
    print('mail send successful')
except smtplib.SMTPException:
    print('error send fail')