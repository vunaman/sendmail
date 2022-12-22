#!/usr/bin/env python3

from email.message import EmailMessage
import ssl
import smtplib

email_sender = "an.vu.k18hcmut@gmail.com"
email_password = "gvvhafnorygketrg"
email_receiver = "an.vu.k18hcmut@gmail.com"

subject = "Email Application Test"
body = """
Hello,

I want to test my new application.
Please reply me when you received this mail.

Cheers,
An.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())