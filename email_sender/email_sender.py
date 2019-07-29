import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import os


class EmailSender:
    """
    A simple abstraction around sending emails
    """

    def __init__(self,
                 sender_email=None,
                 smtp_relay=None,
                 smtp_port=25):

        # sender email
        self.sender_email = sender_email
        self.smtp_relay = smtp_relay
        self.smtp_port = smtp_port

    def send_simple_email(self,
                          recipient: str = '',
                          cc_recipients=[],
                          bcc_recipients=[],
                          subject="[empty subject]",
                          message_contents="[empty message]",
                          attachments=[]):
        """
        Sends simple (i.e. plain text) emails

        :param recipient: a single recipient email string (required)
        :param cc_recipients: a list of cc recipient email strings or empty list
        :param bcc_recipients: a list of strings bcc recipient email or empty list
        :param subject: the message subject line (str)
        :param message_contents: the message (str)
        :param attachments: a list of files to be attached to the email
        :return:
        """
        if isinstance(attachments, str):
            # attachment is a string (i.e. filename), not a list of filenames --> put it in a list
            attachments = [x.strip() for x in attachments.split(',')]
            print(attachments)

        if not isinstance(recipient, str):
            raise ValueError(f"recipient must be a string. Received: {type(recipient)}")

        # Create Email
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.sender_email
        message["To"] = recipient
        if cc_recipients:
            message['Cc'] = ", ".join(cc_recipients)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(message_contents, "plain")
        message.attach(part1)

        # attach the attachments to the email
        # if attachment_file:
        for a in attachments:
            # with open(attachment_file, 'rb') as attachment:
            with open(a, 'rb') as attach_file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attach_file.read())

            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(a)}")
            message.attach(part)

        # Send the email
        server = smtplib.SMTP(self.smtp_relay, self.smtp_port)
        server.connect(self.smtp_relay, self.smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.sendmail(self.sender_email, [recipient] + cc_recipients + bcc_recipients, message.as_string())
        server.quit()


if __name__ == '__main__':
    EmailSender(sender_email=os.environ.get('BEAT_SENDER_EMAIL'),
                smtp_relay=os.environ.get('BEAT_SMTP_RELAY')) \
        .send_simple_email(recipient='david.ostler@advancedmd.com', subject='HOORAY!!')
