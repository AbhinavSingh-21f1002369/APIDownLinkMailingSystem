import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage
# Pulling the credentials from the .env file
load_dotenv()
uid = os.getenv('gmail')
passphrase = os.getenv('password')

def do_mail():
    sub = "AFKZenCoders - API Down"
    body = """Hello there Coder, the API is down
    Check here : http://iot.ccnet.in:1313/logs - nahi chal rha hai"""
    mail_ids = ["21f1002369@student.onlinedegree.iitm.ac.in","21f1003251@student.onlinedegree.iitm.ac.in","21f1000111@student.onlinedegree.iitm.ac.in","aryakesharwani1234@gmail.com"]

    for mail in mail_ids:
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(uid,passphrase)
            msg = EmailMessage()
            msg['Subject'] = sub
            msg['From'] = uid
            msg['To'] = mail
            msg.set_content(body)
            server.send_message(msg)
            print(f"Mail sent to {mail}".format())
            server.quit()
        except Exception as e:
            print(f"Error {e}".format())