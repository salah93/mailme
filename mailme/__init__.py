import smtplib

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List
from os.path import basename


class PayloadBuilder(object):
    def __init__(self, alias_from):
        self.__payload = MIMEMultipart()
        self.__payload["From"] = alias_from

    def add_message(self, message):
        self.__payload.attach(MIMEText(message))
        return self

    def add_attachment(self, attachment):
        with open(attachment, "r") as f:
            app = MIMEApplication(f.read())
        app.add_header(
            "Content-Disposition", "attachment", filename=basename(attachment)
        )
        self.__payload.attach(app)
        return self

    def add_subject(self, subject):
        self.__payload["Subject"] = subject
        return self

    def get_payload(self):
        return self.__payload


class Mail(object):
    def __init__(self, email_address, password):
        self._from = email_address
        self._password = password

    def send(self, to: List[str], payload: MIMEMultipart):
        to = to if isinstance(to, list) else [to]
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as s:
            s.starttls()
            s.login(self._from, self._password)
            return s.sendmail(self._from, to, payload.as_string())
