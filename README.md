# Streambox - Data Science Toolbox

Streambox is a toolbox with a number of functions and decorators useful for data scientists and developers in their projects.

## Installation

You can install this package either by forking this repo and install it locally,
or by installing it directly from PyPip.

### PyPip Installation

```bash
pip install streambox
```

### Local Installation
If you want to hot reload new changes, from repo root run: 

```bash
pip install -e . --upgrade --upgrade-strategy only-if-needed
```
___

# Documentation

Streambox contains the following main namespaces:

- **decorators**: practical decorators
- **tools**: practical functions
- **streamlit**: functions and hacks for Streamlit

## Decorators

### streambox.decorators.cache

> **streambox.decorators.cache**(expiry=datetime.timedelta(minutes=30), persistent=False, ttl=None, no_cache=None, show_log=False)

This decorator cache the result of a function based on the input arguments.
When the function is executed the first time, the result is being cached,
and once it has been called one more time, the cached result would be returned instead of re-executing the function.
The cached data is specific to the function arguments, and once the functions is called with new arguments,
function would be executed and a new cached data will be stored.

By default, all parameters to a cached function must be hashable.
Any parameter whose name begins with _ will not be hashed.
You can use this as an "escape hatch" for parameters that are not hashable

#### Example

```python
import streambox as sb
import logging
import datetime

logging.basicConfig(level=logging.INFO)

@sb.decorators.cache(expiry=datetime.timedelta(seconds=30), persistent=True, ttl=5, show_log=True)
def my_function(arg1, arg2, **kwargs):
    # your function code here
    if some_condition:
        return no_cache
    else:
        if some_other_condition:
            return result1, result2, no_cache
        else:
            return result1, result2
```

```python
import streambox as sb
import datetime

@sb.decorators.cache(expiry=datetime.timedelta(minutes=1), persistent=True, ttl=5)
def foo(x):
    return x + 1

@sb.decorators.cache(expiry=datetime.timedelta(minutes=1), persistent=False, ttl=5)
def bar(x, y):
    return x * y
```

### streambox.decorators.retry

> **streambox.decorators.retry**(max_tries=5, delay_seconds=None, incremental_delay=10)

This decorator retry function in case of failure.

#### Parameters

- **max_tries** (int) (default: `5`)

  This the maximum number of tries. The default value is 5.

- **delay_seconds** (int) (default: `None`)

  This is delay/wait in seconds between each try. If not provided, the default value is None,
and it checks `incremental_delay`.

- **incremental_delay** (int) (default: `10`)

  This is a factor in delay between each try if `delay_seconds` is `None`.
The default value is 10 seconds. It means that if the function fails, the next try happens in 10 seconds.
If it fails again, it adds another 10 seconds to the previous delay, which makes it 20 seconds.

#### Example

```python
import streambox as sb


@sb.decorators.retry(max_tries=5, delay_seconds=None)
def run_my_function(result):
    print("Function started")
    raise Exception("This is a custom error!")
    return result
```

### streambox.decorators.logger

> **streambox.decorators.logger**(timer=False)

This decorator logs the beginning and the end of function execution with the execution time.

#### Parameters

- **timer** (boolean) (default: `False`)

  If `timer` is set to `True`, it will show the execution time of the function.

#### Example

```python
import streambox as sb
import time


@sb.decorators.logger(timer=True)
def run_my_function(result):
    print("Function started")
    time.sleep(2)
    return result
```

### streambox.decorators.email_on_failure

> **streambox.decorators.email_on_failure**(from_email, to_email, smtp_server, smtp_port, username, password)

This decorator sends an email using SMTP settings if there is a failure inside a function.

#### Parameters

- **sender_email** (string)

  The email address of the sender.

- **receiver_email** (string)

  The email address of the receiver.

- **subject** (string)

  The subject of the email.

- **message** (string)

  The body of the email.

- **smtp_server** (string)

  The SMTP server hostname or IP address.

- **smtp_port** (int)

  The SMTP server port number.

- **smtp_username** (string)

  The username to authenticate with the SMTP server.

- **smtp_password** (string)

  The password to authenticate with the SMTP server.


#### Example
Here's an example of using the send_email function to send an email:

```python
import streambox as sb


sender_email = 'sender@example.com'
receiver_email = 'receiver@example.com'
subject = 'Test email'
message = 'This is a test email sent from Python!'
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'username'
smtp_password = 'password'

@sb.decorators.email_on_failure(sender_email, receiver_email,
                                subject, message,
                                smtp_server, smtp_port,
                                smtp_username, smtp_password)
def sample_function():
    # this is failure by division by zero
    print(1/0)
```

___
## Tools

### streambox.tools.flush_cache

> **streambox.tools.flush_cache**()

This decorator flush the persistent cache data files in the package.

___
## Streamlit

### Session
### streambox.session.get_session_id

> **streambox.session.get_session_id**()

This returns the active session ID of the current user.

#### Example
```python
import streambox as sb


session_id = sb.session.get_session_id()
print(session_id)
```

### streambox.session.get_user_info

> **streambox.session.get_user_info**()

This returns the current user information (such as email address), if the user is accessed via Streamlit Cloud.

#### Example
```python
import streambox as sb


user_info = sb.session.get_user_info()
print(user_info)
```

### streambox.session.get_all_sessions

> **streambox.session.get_all_sessions**()

This returns a list of all active session IDs.

#### Example
```python
import streambox as sb


sessions = sb.session.get_all_sessions()
print(sessions)
```

### Style
### streambox.style.hide_footer

> **streambox.style.hide_footer**()

This function injects a CSS to hide footer in Streamlit.

#### Example
```python
import streamlit as st
import streambox as sb


sb.style.hide_footer()
```

### streambox.style.hide_hamburger_menu

> **streambox.style.hide_hamburger_menu**()

This function injects a CSS to hide hamburger menu in Streamlit.

#### Example
```python
import streamlit as st
import streambox as sb


sb.style.hide_hamburger_menu()
```

### streambox.style.hide_default_radio_selection

> **streambox.style.hide_default_radio_selection**()

This function injects a CSS to hide the first item in `st.radio` in Streamlit.
This would allow developers to have radio buttons without default value.
In order to use this, the first element of the radio button should be an arbitrary item. 

#### Example
```python
import streamlit as st
import streambox as sb


options = ["-", "Item 1", "Item 2"]
item = st.radio("Radio", options=options)

# this function hides the first radio option which is selected by default
sb.style.hide_default_radio_selection()
```

___
## GitHub Repo
This project is open-source, and it is available on GitHub at [https://github.com/kavehbc/streambox](https://github.com/kavehbc/streambox).

## Developer(s)
- Kaveh Bakhtiyari - [Website](https://bakhtiyari.com) | [Medium](https://medium.com/@bakhtiyari)
  | [LinkedIn](https://www.linkedin.com/in/bakhtiyari) | [GitHub](https://github.com/kavehbc)

- ChatGPT, OpenAI - [Website](https://openai.com)

___
## Changelog
- **0.1.0** (23 March 2023)

    This is the genesis version released.
