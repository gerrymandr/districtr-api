from flask import current_app
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Content, Email, Mail

from .exceptions import ApiException


def send_email(from_address, to_address, subject, body):
    mail = Mail(
        Email(from_address, name="Districtr"),
        subject,
        Email(to_address),
        Content("text/html", body),
    )

    if current_app.config.get("SEND_EMAILS", True) is False:
        print("Sending mail", mail)
        return

    client = SendGridAPIClient(api_key=current_app.config["SENDGRID_API_KEY"]).client
    response = client.mail.send.post(request_body=mail.get())

    if response.status_code >= 300:
        raise ApiException("Unable to send email.", status=500)
