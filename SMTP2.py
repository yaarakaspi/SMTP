import smtplib
from email.message import EmailMessage
from smtplib import SMTP


msg = EmailMessage()
sender = input("enter sender's mail address: ")
password = input("enter sender's password: ")
receiver = input("enter receiver's address: ")
msg['Subject'] = 'שליחת SMTP עם קובץ מיואב פיינר'
msg['From'] = sender
msg['To'] = receiver
msg.set_content('תתכוננו לבדיחה המצחיקה בעולם')
with open('joke.txt', 'rb') as f:
    file_data = f.read()
    file_name = f.name
msg.add_attachment(file_data, maintype='text', subtype='plain', filename=file_name)
try:
    server = smtplib.SMTP('smtp.gmail.com', 25)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()
    print("email sent")
except Exception as e:
    print(f"Error message didn't get sent {e}")