
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#smtplib是python的一个内置库，所以不需要用pip安装
mailhost='smtp.qq.com'
#把qq邮箱的服务器地址赋值到变量mailhost上
qqmail = smtplib.SMTP()
#实例化一个smtplib模块里的SMTP类的对象，这样就可以SMTP对象的方法和属性了
qqmail.connect(mailhost,25)
#连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
#以上，皆为连接服务器的代码

sender = "285022155@qq.com"
#获取邮箱账号
password = "fejadnebnzuqbgfd"
#获取邮箱密码
# qqmail.login(account, 'fejadnebnzuqbgfd')
#登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码
qqmail.login(sender,password)

receiver="xsx0721@163.com"
#获取收件人的邮箱


content="test内容"
message = MIMEText(content, 'plain', 'utf-8')
subject ="邮件主题："
message['Subject'] = Header(subject, 'utf-8')
#在等号的右边，是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']。

qqmail.sendmail(sender, receiver, message.as_string())
#发送邮件，调用了sendmail()方法，写入三个参数，分别是发件人，收件人，和字符串格式的正文。
qqmail.quit()
#退出邮箱