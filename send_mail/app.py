import os
import mail as m
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('EMAIL')
email_pwd = os.getenv('EMAIL_PWD')
recipient = os.getenv('RECIPIENT')
subject = 'Testing from Python'

m.send_mail(email, email_pwd, recipient, subject, 'this is a test')