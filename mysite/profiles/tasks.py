from __future__ import absolute_import, unicode_literals

from celery import shared_task
# from .models import Widget

from time import sleep
# from celery import Celery
# app = Celery('tasks', broker='redis://localhost')
# @app.task
@shared_task
def sleepy(duration):
	sleep(duration)
	return None




@shared_task
def add(x, y):
    return x + y
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='agboemmanuel002@gmail.com',
    to_emails='ruthozioma1997@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
