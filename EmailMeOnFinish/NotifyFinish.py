#!/usr/bin/env python3
"""
Send email via Gmail SMTP
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def notify_finish(sender_email, receiver_email, app_password, subject="", text="", body_type="plain"):
    """
    Send email via Gmail SMTP

    Parameters
    ----------
    sender_email : str
    receiver_email : str or list[str]
    app_password : str
        App password for Gmail SMTP
    subject : str, optional
    text : str, optional
    body_type : str, optional
        Either "plain" or "html"
    """

    message = MIMEMultipart("alternative")

    default_msg = "Your job is finished."
    if subject == "":
        subject = default_msg
    if text == "":
        text = default_msg

    message["Subject"] = subject
    message["From"] = sender_email
    if isinstance(receiver_email, list):
        message["To"] = ", ".join(receiver_email)
    elif isinstance(receiver_email, str):
        message["To"] = receiver_email
    else:
        message["To"] = sender_email
        print("receiver_email is not a list or string. Used sender_email instead.")

    body = MIMEText(text, body_type)

    message.attach(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        try:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Successfully sent email")
        except Exception as e:
            print("Error: unable to send email")
            print(e)