# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def house_Loan():
    msg_from = '18339443137@163.com'
    passwd = 'NHIKXMZGJVRSLSJY'   # 163邮箱授权码
    # passwd = 'vtawjlgwoxwseabb' # qq邮箱授权码
    msg_to = '2623961667@qq.com'
    msg = MIMEText('this is a test !')
    msg['Subject'] = '房贷还款提醒邮件'
    msg['from'] = msg_from
    msg['to'] = msg_to
    try:
        s = smtplib.SMTP_SSL('smtp.163.com',465)
        s.login(msg_from,passwd)
        s.sendmail(msg_from,msg_to,msg.as_string())
        print('发送成功')
    except Exception as e:
        print(e)
    finally:
        s.quit()

if __name__ == '__main__':
    house_Loan()
