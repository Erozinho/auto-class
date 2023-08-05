import yagmail
from time import sleep

sender = 'felipe9a.cva@gmail.com'
receiver = 'zenycsoficial@gmail.com'

subject = 'EMAIL TESTE!'

content = """
EMAIL TESTE FAVOR IGNORAR!
"""
while True:
    sleep(60)
    yag = yagmail.SMTP(user=sender, password=input('Your Password:\n'))
    yag.send(to=receiver,subject=subject,contents=content)
    print('Email Sent!')