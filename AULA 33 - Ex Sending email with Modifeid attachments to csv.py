import yagmail
from time import sleep
import pandas

sender = 'felipe9a.cva@gmail.com'
receiver = 'zenycsoficial@gmail.com'
password = input('Your Password:\n')

yag = yagmail.SMTP(user=sender, password=password)

df = pandas.read_csv('auto-class/contacts.csv')

def generate_file(filename, content):
        with open(f"auto-class/{filename}.txt", 'w', encoding='UTF-8') as file:
            file.write(f"{filename} você precisa pagar {content}$ até o fim do dia!")

for index, row in df.iterrows():
    name = row['name']
    amount = row['amount']
    receiver_mail = row['email']

    generate_file(name, amount)

    subject = f"EMAIL TESTE para {name}!"

    content = [f"""
               OLA {name}, isso é um EMAIL TESTE FAVOR IGNORAR!
               """, f'auto-class\\{name}.txt']
    yag.send(to=receiver_mail,subject=subject,contents=content)
print('Emails Sent!')