import traceback
from streambox.lib.email import send_email


def email_on_failure(from_email, to_email, smtp_server, smtp_port, username, password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # format the error message and traceback
                err_msg = f"Error: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
                msg_subject = f"{func.__name__} failed"

                send_email(from_email, to_email, subject=msg_subject, body=err_msg,
                           smtp_server=smtp_server, smtp_port=smtp_port,
                           username=username, password=password)

                # re-raise the exception
                raise

        return wrapper

    return decorator
