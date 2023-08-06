import yagmail
from time import sleep
import pandas

sender = 'felipe9a.cva@gmail.com'
receiver = 'zenycsoficial@gmail.com'
password = input('Your Password:\n')

yag = yagmail.SMTP(user=sender, password=password)

df = pandas.read_csv('auto-class/contacts.csv')

for index, row in df.iterrows():
    subject = f"EMAIL TESTE para {row['name']}!"

    text = f"""OLA {row['name']}, isso é um EMAIL TESTE FAVOR IGNORAR!"""
    content = [text, 'auto-class\\contacts.csv']
    yag.send(to=row['email'],subject=subject,contents=content)
print('Emails Sent!')