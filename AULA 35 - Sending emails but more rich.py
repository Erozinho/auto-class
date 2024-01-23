import smtplib

sender = 'mateus_eausp@hotmail.com.br'
receiver = 'felipe9a.cva@gmail.com'
password = input('Password here:\n')

message = """\
Subject: EMAIL DE TESTE!

Este eh uma email de teste!
"""

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
