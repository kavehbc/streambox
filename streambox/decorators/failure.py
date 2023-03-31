import traceback
import logging
from streambox.tools.comm import send_email
from streambox.tools.comm import slack_notify


logging.basicConfig(level=logging.INFO)


def notify_on_failure(email_settings: dict = None,
                      slack_settings: dict = None,
                      show_log=False):
    """
    This decorator sends a notification if there is an exception raised within the function.

    :param email_settings: A dictionary containing the SMTP email settings.
        E.g.
            email_settings = {"from": "test@email.com",
                              "to": "admin@email.com",
                              "smtp_server": "mail.email.com",
                              "smtp_port": 587,
                              "username": "admin",
                              "password": "sample_password"}
    :param slack_settings: A dictionary containing Slack channel settings.
        E.g.
            slack_settings = {"url": "http://slack_webhook_address",
                              "username": "test_user",
                              "attachments": None}
    :param show_log: A boolean to show logging details
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # format the error message and traceback
                err_msg = f"Error: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
                msg_subject = f"{func.__name__} failed"

                if email_settings is not None:
                    # send email
                    if show_log:
                        logging.info(f'Sending email')
                    send_email(email_settings["from"], email_settings["to"],
                               subject=msg_subject, body=err_msg,
                               smtp_server=email_settings["smtp_server"], smtp_port=email_settings["smtp_port"],
                               username=email_settings["username"], password=email_settings["password"])
                if slack_settings is not None:
                    # send Slack message
                    if show_log:
                        logging.info(f'Notifying on Slack')
                    slack_notify(url=slack_settings["url"], msg=err_msg,
                                 attachments=slack_settings["attachments"], username=slack_settings["username"])
                # re-raise the exception
                raise

        return wrapper

    return decorator
