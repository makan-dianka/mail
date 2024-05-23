#!/usr/bin/env python3

import config
import dotenv
import os
import sys
import design

gmail = config.SenderGmail()
file = gmail.check_exist_or_empty_file('.env')

dotenv.load_dotenv(file)

sender = os.getenv('GMAIL')
password = os.getenv('PASSWORD')

HELP="\nDo you need help ? use: --help\n\n python3 sendmail.py --help\n"

if '@gmail' not in sender:
    print("""

        This program required adress mail of google. eg. @gmail.com
        Please give a gmail adress.


        Author : Makan
        Email  : python3.230492@gmail.com
        web    : makandianka.com

    """)

    exit()


if __name__ == '__main__':

    params = sys.argv

    if len(params) == 4:
        main_file, params_1, params_2, params_3 = params[0], params[1], params[2], params[3]
        subject, subject_ = params_1.split("=")
        body, content = params_2.split("=")
        sendto, mail = params_3.split("=")
        
        if subject.lower() == 'subject' and body.lower() == 'body' and sendto.lower() == 'sendto':
            
            gmail.send(
                sender=sender, password=password,
                recever=mail,
                subject=subject_,
                message=content
            )

        else:
            print(HELP)
    
    elif len(params) == 5:
        main_file, file, params_2, params_3, params_4 = params[0], params[1], params[2], params[3], params[4]
        subject, subject_file = params_2.split("=")
        body, content_file = params_3.split("=")
        sendto, mail_file = params_4.split("=")
        
        if file.lower() == "--files":
            if subject.lower() == 'subject' and body.lower() == 'body' and sendto.lower() == 'sendto':
                mails = gmail.get_mails(mail_file)
                for mail in mails:
                    gmail.send(
                        sender=sender, password=password,
                        recever=mail,
                        subject=gmail.get_file_content(subject_file),
                        message=gmail.get_file_content(content_file)
                    )
            else:
               print(HELP) 
        else:
            print(HELP)

    elif len(params) == 2 and params[1] == '--help':
        design.help()

    else:
        print(HELP)
