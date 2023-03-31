import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(sender_email, receiver_email, cc=None, bcc=None, subject='', message='', attachments=None,
               smtp_server='', smtp_port: int = 587, smtp_username='', smtp_password='', plain_text=True, priority=3):
    """Send an email using SMTP.

    Parameters:
    sender_email (str): The email address of the sender.
    receiver_email (str): The email address of the receiver.
    cc (list[str]): A list of email addresses to carbon copy. Defaults to None.
    bcc (list[str]): A list of email addresses to blind carbon copy. Defaults to None.
    subject (str): The subject of the email. Defaults to ''.
    message (str): The body of the email. Defaults to ''.
    attachments (list[str]): A list of file paths to attach to the email. Defaults to None.
    smtp_server (str): The hostname or IP address of the SMTP server. Defaults to ''.
    smtp_port (int): The port number of the SMTP server. Defaults to 587.
    smtp_username (str): The username to use for SMTP authentication. Defaults to ''.
    smtp_password (str): The password to use for SMTP authentication. Defaults to ''.
    plain_text (bool): Whether the message is in plain text format. Defaults to True.
    priority (int): The priority level of the message, between 1 (highest) and 5 (lowest). Defaults to 3.

    Returns:
    None.

    Raises:
    Exception: If there is an error sending the email.

    """

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add CC to email
    if cc:
        msg['CC'] = ', '.join(cc)

    # Add BCC to email
    if bcc:
        msg['BCC'] = ', '.join(bcc)

    # Add body to email
    if plain_text:
        msg.attach(MIMEText(message, 'plain'))
    else:
        msg.attach(MIMEText(message, 'html'))

    # Add attachments to email
    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as f:
                part = MIMEApplication(f.read(), Name=attachment.split('/')[-1])
                part['Content-Disposition'] = f'attachment; filename="{attachment.split("/")[-1]}"'
                msg.attach(part)

                # Set message priority
                if priority:
                    # Map priority level to X-Priority header value
                    priority_levels = {1: '1 (Highest)', 2: '2 (High)', 3: '3 (Normal)', 4: '4 (Low)', 5: '5 (Lowest)'}
                if priority not in priority_levels:
                    raise ValueError(f"Invalid priority level '{priority}'. Must be between 1 and 5.")
        msg['X-Priority'] = priority_levels[priority]

    # Open SMTP connection and send email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(sender_email, [receiver_email] + (cc or []) + (bcc or []), text)
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        raise e


def send_gmail(receiver_email, cc=None, bcc=None,
               subject='', message='', attachments=None,
               smtp_username=None,
               smtp_password=None,
               plain_text=True, priority=3):

    """
    An Email wrapper for GMail
    """

    # Gmail SMTP Settings
    if smtp_username.endswith('@gmail.com'):
        sender_email = smtp_username
    else:
        sender_email = smtp_username + "@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    send_email(sender_email=sender_email, receiver_email=receiver_email,
               cc=cc, bcc=bcc, subject=subject, message=message, attachments=attachments,
               smtp_server=smtp_server,
               smtp_port=smtp_port, smtp_username=smtp_username, smtp_password=smtp_password,
               plain_text=plain_text, priority=priority)
