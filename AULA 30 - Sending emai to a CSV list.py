import yagmail
import pandas

sender = 'felipe9a.cva@gmail.com'
password = input('type your password:\n')

df = pandas.read_csv('automations-lessons\\contacts.csv')

for index, row in df.iterrows():
    subject = 'EMAIL TESTE!'

    content = (f"""
    Ola, {row['name']}, ISSO É UM EMAIL TESTE FAVOR IGNORAR!
    """)

    yag = yagmail.SMTP(user=sender, password=password)
    yag.send(to=row['email'],subject=subject,contents=content)
    print('Email Sent!')