#!/usr/bin/env python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import dotenv
import os

dotenv.load_dotenv('./.env')

sender = os.getenv('sender')
password = os.getenv('password')

if 'gmail' not in sender:
    print("""

        This program required adress mail of google. eg. @gmail.com
        Please give a gmail adress.


        Author : Makan
        Email  : python3.230492@gmail.com
        web    : makandianka.org

    """)

    exit()

def connexion(mail, pwd):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(mail, pwd)
    except Exception as e:
        print("\n\033[31mLogin failed.\n\033[33m")
        print(e, '\n')
        exit()
    else:
        # print("login success !")
        return server

def readmails(mails:list)->list:
    """takes empty list. return list with mails"""
    with open('mails.txt', 'r') as mails_file:
        lines = mails_file.readlines()
        for mail in lines:
            mails.append(mail.strip())

    return mails


def readmessage():
    with open('message.txt', 'r') as message:
        return message.read()

def readsubject():
    with open('subject.txt', 'r') as subject:
        return subject.read()


def send(recever, subject, message):
    mail=MIMEMultipart()
    mail['From'] = sender
    mail['To'] = recever
    mail['Subject'] = subject
    
    mail.attach(MIMEText(message,'plain'))
    text = mail.as_string()

    server = connexion(sender, password)
    try:
        server.sendmail(sender,recever,text)
    except Exception as e:
        print(e)
    else:
        print(f"[OK] Message envoyé à : {recever}")
        server.quit() 

mails = readmails([])
subj = readsubject()
msg = readmessage()

for mail in mails:
    send(mail, subj, msg)