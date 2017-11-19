import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'zsl970214@126.com'
msg['to'] = '805043442@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com', '25')
smtp.login('zsl970214@126.com', '970214.')
smtp.sendmail('zsl970214@126.com', '805043442@qq.com', str(msg))
smtp.quit()