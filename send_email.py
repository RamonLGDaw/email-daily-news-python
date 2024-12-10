import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sending_email(message):
    host = 'smtp.gmail.com'
    port = 465
    password = os.getenv('PASSWORD')
    username = 'mispruebasweb24@gmail.com'
    receiver = 'mispruebasweb24@gmail.com'
    context = ssl.create_default_context()

    # Crear un mensaje MIME con contenido UTF-8
    mime_message = MIMEMultipart()
    mime_message['From'] = username
    mime_message['To'] = receiver
    mime_message['Subject'] = 'Daily news from Python App!!'

    # Adjuntar el mensaje como texto plano codificado en UTF-8
    mime_message.attach(MIMEText(message, 'plain', 'utf-8'))

    # Enviar el correo
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, mime_message.as_string())
