from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message['From'] = 'Ananta'
message['To'] = 'anantajoy007@gmail.com'
message['Subject'] = 'This is a test email'

body = 'This is a test email. Please ignore it.'

message.attach(MIMEText(body, 'plain'))

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('s1810174145@ru.ac.bd','nf89vn6@rc4%')
    smtp.send_message(message)
    print('Sent Successfully')
