
def help():
    print(
        """
        Usage: python3 sendmail.py

        +----------------------------------------------------+
        | send email to a single one personne                |
        +----------------------------------------------------+

        python3 sendmail.py [subject=subject] [body=messagecontent] [sendto=emailtosend]

        +-----------------------------------------------------+
        | send email to many personne. (require to use files) |
        +-----------------------------------------------------+

        use flag: --files and specify path to your files.

        python3 sendmail.py [--files] [subject='/path/to/subject.txt file'] [body=/path/to/message.txt file] [sendto=/path/to/mails.txt file]

        """
    )