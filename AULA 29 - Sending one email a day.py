import yagmail
from time import sleep
from datetime import datetime as dt

sender = 'felipe9a.cva@gmail.com'
receiver = 'felipe9a.cva@gmail.com'

subject = 'EMAIL TESTE!'

content = """
EMAIL TESTE FAVOR IGNORAR!
"""
while True:
    now = dt.now()
    if now.hour == 13:
        sleep(3600)
        yag = yagmail.SMTP(user=sender, password=input('Your Password:\n'))
        yag.send(to=receiver,subject=subject,contents=content)
        print('Email Sent!')