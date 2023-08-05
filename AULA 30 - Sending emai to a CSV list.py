import yagmail
import pandas

sender = 'felipe9a.cva@gmail.com'
password = input('type your password:\n')

subject = 'EMAIL TESTE!'

df = pandas.read_csv('automations-lessons\\contacts.csv')

yag = yagmail.SMTP(user=sender, password=password)

for index, row in df.iterrows():
    content = (f"""
    Ola, {row['name']}, ISSO É UM EMAIL TESTE FAVOR IGNORAR!
    """)

    yag.send(to=row['email'],subject=subject,contents=content)
print('Emails Sent!')
