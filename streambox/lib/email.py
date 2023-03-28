import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(from_email, to_email, subject, body, smtp_server, smtp_port, username, password):
    """
    Sends an email with the given parameters using SMTP settings.
    """

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(body, 'plain'))

    # Open SMTP connection and send email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print('Something went wrong: ' + str(e))
