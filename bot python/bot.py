import os 
import smtplib
from email.message import EmailMessage

# configuração de e-mail e senha

SEU_EMAIL = 'digite seu email aqui'
SUA_SENHA = 'digite sua senha aqui'

# criação de um e-mail
message = EmailMessage()
message ['Subject'] = 'digite o título/tópico do email.'
message ['From'] = 'digite novamente seu e-mail neste campo.'
message ['To'] = 'digite o e-mail do destinatário neste campo.'
message.set_content ('digite sua mensagem neste campo.')

# enviar o e-mail

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(SEU_EMAIL, SUA_SENHA)
    smtp.send_message(message)
