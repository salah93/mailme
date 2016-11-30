#! /usr/local/bin/python


def mailto(to, msg, subject=''):
    from contextlib import contextmanager 
    from .credentials import myemail, mypassword
    msg = 'Subject: {subject}\n\n{body}'.format(subject=subject, body=msg)
    @contextmanager
    def login(email, password):
        import smtplib
        # port 465 or 587
        port = 587
        try:
            server = smtplib.SMTP('smtp.gmail.com', port) 
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(myemail, mypassword)
            server.sendmail
            yield server
        finally:
            server.quit()
    with login(myemail, mypassword) as s:
        s.sendmail(myemail, to, msg)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('TO')
    parser.add_argument('MSG')
    parser.add_argument('--subject', default='')
    args = parser.parse_args()
    mailto(args.TO, args.MSG, args.subject)
