[![Build Status](https://travis-ci.com/dro248/email_sender.svg?branch=master)](https://travis-ci.com/dro248/email_sender)
# email_sender

## Install
```bash
pip install git+https://github.com/dro248/email_sender.git@master#egg=email_sender
```
> Note: Written for Python3.6+


## Usage
```python
from email_sender.email_sender import EmailSender

sender = EmailSender(sender_email='my@email.com', 
            smtp_relay='smtprelay.mydomain.com')

sender.send_simple_email(recipient='my@email.com', 
                         cc_recipients=['friend1@gmail.com', 'friend2@gmail.com'],
                         bcc_recipients=['blind_friend1@gmail.com'],
                         subject='My Subject',
                         message_contents='Hello World!',
                         attachments=['file1.txt', 'file2.csv'])
```
