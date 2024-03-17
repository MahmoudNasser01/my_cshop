import os
from threading import Thread

from django.core.mail import EmailMultiAlternatives

"""
usage:
        EmailThread(
            subject="Monthly Subscriptions Report",
            message="Monthly Subscriptions Report attached",
            html_message="Monthly Subscriptions Report attached",
            attachments=mail_attachments,
            to_email=emails[0],
            cc_arr=emails[1:],
        ).start()
"""


class EmailThread(Thread):
    def __init__(self, subject, message, to_email, html_message,
                 reply_to=os.environ.get('INFO_EMAIL', 'tech@fitpass.ch'), attachments=None, cc_arr=None):
        super().__init__()
        self.subject = subject
        self.message = message
        self.from_email = os.environ.get('EMAIL_HOST_USER', 'noreply@cshop.com')
        self.to_email = to_email
        self.reply_to = reply_to
        self.html_message = html_message
        self.attachments = attachments
        self.cc = cc_arr

    def run(self):

        mail = EmailMultiAlternatives(
            self.subject,
            self.message,
            to=[self.to_email],
            from_email="FITPASS AG <" + self.from_email + ">",
            reply_to=[self.reply_to],
            cc=self.cc
        )
        mail.attach_alternative(self.message, 'text/html')
        if self.attachments is not None:
            for attachment in self.attachments:
                mail.attach(content=attachment['content'], filename=attachment['name'])
        mail.send(fail_silently=False)
