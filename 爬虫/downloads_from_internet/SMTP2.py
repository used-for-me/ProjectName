import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

ISOTIMEFORMAT = '%Y%m%d'


def sent_email(name, context):
    global flag
    flag = 0
    caodate = str(time.strftime(ISOTIMEFORMAT, time.localtime()))
    # 设置发件服务器地址
    host = 'smtp.qq.com'
    # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
    port = 465

    # 设置发件邮箱，一定要自己注册的邮箱
    sender = '3377633913@qq.com'
    # 设置发件邮箱的密码，qq邮箱的授权码，等会登陆会用到
    pwd = '************'
    # 设置邮件接收人，可以是扣扣邮箱
    receiver0 = '1378336117@qq.com'
    # 设置邮件正文，这里是支持HTML的
    body = '<h1>' + name + '</h1><p>'+str(context)+' </p>'
    # 设置正文为符合邮件格式的HTML内容
    msg = MIMEText(body, 'html')
    message = MIMEMultipart()
    # 设置邮件标题
    message['subject'] = caodate + name
    # 设置发送人
    message['from'] = sender
    # 设置接收人
    message['to'] = receiver0
    # 构造附件1，传送当前目录下的 filename 文件
    message.attach(msg)
    print(3)
    # att1 = MIMEText(context, 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    #
    # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # att1["Content-Disposition"] = 'attachment; filename="' + value + '"'

    # message.attach(att1)

    def ready_send():
        global flag
        try:
            print(4)
            s = smtplib.SMTP_SSL(host, port)
            # s = smtplib.SMTP_SSL(host, port)  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
            print(5)
            s.login(sender, pwd)  # 登陆邮箱
            print(6)
            s.sendmail(sender, receiver0, message.as_string())  # 发送邮件！
            print(7)
            # s.sendmail(sender, receiver0, msg.as_string())
            print('Done.sent email success')
            flag = 0
        except smtplib.SMTPException as e:
            print('Error.sent email fail')
            flag += 1

    ready_send()
    while 0 < flag <= 10:
        time.sleep(20)
        print('sleep')
        ready_send()
    return flag


