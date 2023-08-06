import yagmail
from time import sleep

sender = 'felipe9a.cva@gmail.com'
receiver = 'felipe9a.cva@gmail.com'
password = input('Your Password:\n')

subject = 'EMAIL TESTE!'

content = ["""
EMAIL TESTE FAVOR IGNORAR!
""", 'auto-class\\contacts.csv']

yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver,subject=subject,contents=content)
print('Email Sent!')