#! /usr/local/bin/python
import smtplib
import sys
from contextlib import contextmanager 

from credentials import myemail, mypassword


@contextmanager
def login(email, password):
    # port 465 or 587
    port = 587
    try:
        server = smtplib.SMTP('smtp.gmail.com', port) 
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(myemail, mypassword)
        yield server
    finally:
        server.close()


def mailto(to, msg):
    with login(myemail, mypassword) as s:
        s.sendmail(myemail, to, msg)


if __name__ == '__main__':
    to, msg = sys.argv[1:]
    mailto(to, msg)
