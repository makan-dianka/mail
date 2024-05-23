import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


class SenderGmail:

    def connect_to_gmail(self, user_email,  user_password):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(user_email, user_password)
        except Exception as e:
            print("\n\033[31mLogin failed.\n\033[33m")
            print(e, '\n')
            exit()
        else:
            print("login success !")
            return server


    def check_exist_or_empty_file(self, filename):
        file_stat = os.path.isfile(filename) and os.path.getsize(filename) > 0
        if file_stat == False:
            print(f"\n\033[31mCe fichier n'existe pas ou vide: {filename}\033[33m\n")
            exit()
        return filename


    def get_mails(self, file_mails)->list:
        """return list with mails from file_mails"""
        file = self.check_exist_or_empty_file(file_mails)
        with open(file, 'r') as mails_file:
            mails = [mail.strip() for mail in mails_file.readlines()] 
            return mails
    

    def get_file_content(self, filename):
        file = self.check_exist_or_empty_file(filename)
        with open(file, 'r') as file:
            file_content = file.read()
            return file_content


    def send(self, **kwargs):
        """
        kwargs: sender=email, password=password, recever=recever, subject=subject, message=message
        """

        # user authentication to gmail account data
        sender = kwargs.get('sender')
        password = kwargs.get('password')

        # message data 
        recever = kwargs.get('recever')
        subject = kwargs.get('subject')
        message = kwargs.get('message')


        mail=MIMEMultipart()
        mail['From'] = sender
        mail['To'] = recever
        mail['Subject'] = subject
        
        mail.attach(MIMEText(message,'plain'))
        text = mail.as_string()

        server = self.connect_to_gmail(sender, password)

        try:
            server.sendmail(sender,recever,text)
        except Exception as e:
            print(f'\nerror: {e}\n\n')
        else:
            print(f"[OK] Message envoyé à : {recever}")
            print("--" * 10)
            server.quit()
