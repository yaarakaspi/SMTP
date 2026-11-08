import smtplib
from email.message import EmailMessage
from smtplib import SMTP


msg = EmailMessage()
sender = input("enter sender's mail address: ")
password = input("enter sender's password: ")#ppje bnwn ntai gyeo
receiver = input("enter receiver's address: ")
msg['Subject'] = 'שליחת SMTP מיואב פיינר'
msg['From'] = sender
msg['To'] = receiver
msg.set_content('איש צמחוני הלך הלך הלך בום שניצל תירס עם קטשופ')
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