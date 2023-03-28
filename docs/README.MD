# Streamkit Documentations

## decorators

### sk.decorators.cache

```python
import streambox as sb


@sb.decorators.cache
def run_my_function(result, _check=False):
    print("Print from inside function only runs the first time")
    return result * 2


result = run_my_function(5, _check=True)
print("Result: ", result)
```


### sk.decorators.retry

sk.decorators.retry(max_tries=5, delay_seconds=None, incremental_delay=10)

```python
import streambox as sb


@sb.decorators.retry(max_tries=5, delay_seconds=None)
def run_my_function(result):
    print("Function started")
    raise Exception("This is a custom error!")
    return result
```

### sk.decorators.timer

timer(msg_template=None,
          level=logging.INFO,
          prefix=None,
          suffix=None,
          logger=logger_default)

```python
import streambox as sb
import time


@sb.decorators.timer()
def run_my_function(result):
    print("Function started")
    time.sleep(2)
    return result
```

### sk.decorators.logger

```python
import streambox as sb
import time


@sb.decorators.logger
def run_my_function(result):
    print("Function started")
    time.sleep(2)
    return result
```

### sk.decorators.email_on_failure

The send_email function is a Python function that can be used to send an email using SMTP settings. It takes the following parameters:

- sender_email (string): The email address of the sender.
- receiver_email (string): The email address of the receiver.
- subject (string): The subject of the email.
- message (string): The body of the email.
- smtp_server (string): The SMTP server hostname or IP address.
- smtp_port (int): The SMTP server port number.
- smtp_username (string): The username to authenticate with the SMTP server.
- smtp_password (string): The password to authenticate with the SMTP server.

#### Usage
To use the send_email function, call it with the required parameters like this:

Make sure to replace the sender email, receiver email, SMTP server, SMTP port, SMTP username, and SMTP password with the appropriate values for your email account and SMTP server.


sk.decorators.email_on_failure(from_email, to_email, smtp_server, smtp_port, username, password)

#### Example
Here's an example of using the send_email function to send an email:

```python
sender_email = 'sender@example.com'
receiver_email = 'receiver@example.com'
subject = 'Test email'
message = 'This is a test email sent from Python!'
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'username'
smtp_password = 'password'

send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password)

```

#### Dependencies

The send_email function requires the following dependencies:

- smtplib: This is a Python library for sending emails using the Simple Mail Transfer Protocol (SMTP).
- email.mime.text: This is a Python library for creating MIME text messages.
- email.mime.multipart: This is a Python library for creating MIME multipart messages.


## Streamlit

### Sessions

from streamkit.streamlit.session import get_all_sessions, get_session_id, get_user_info


