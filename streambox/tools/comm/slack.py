import requests
import json


def slack_notify(url, message, attachments=None, username='DataScience'):
    """
    This function sends a message to a Slack channel via a Webhook URL

    :param url: Slack Webhook URL (e.g. "https://hooks.slack.com/services/SOME_TOKEN")
    :param message: Message body to be sent
    :param attachments: Message attachments
    :param username: Username
    """
    #

    payload = json.dumps(
        {
            'text': message,
            'username': username,
            'attachments': attachments
        }
    )

    headers = {
        'Content-Type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code != 200:
        raise ValueError(
           'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
    return response
