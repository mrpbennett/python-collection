import smtplib
from simple_chalk import chalk, green, red


def send_mail(user, pwd, recipient, subject, body):

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # prepare actual message
    message = """From %s\nTo: %s\nSubject: %s\n\n%s""" % (
        FROM,
        ",".join(TO),
        SUBJECT,
        TEXT,
    )

    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.login(user, pwd)
        server_ssl.sendmail(FROM, TO, message)
        server_ssl.close()
        print("You message was sent, succesfully")
    except:
        print("You message failed to send!")

