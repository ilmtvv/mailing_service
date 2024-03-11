from email.message import EmailMessage

from config import settings
import smtplib

from logs.models import Log


def email_post(subject, message, recipient_list, mailing_object):   # проблемы с безопасностью
    from_email = settings.EMAIL_HOST_USER
    password_from_email = settings.EMAIL_HOST_PASSWORD

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject

    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.login(from_email, password_from_email)

    try:
        server.sendmail(from_email, recipient_list, msg.as_string())
        log = Log.objects.create(mailing=subject, user=mailing_object.users, responce_mailing='OK', responce_server='OK')
        return log.save()
    except Exception as e:
        log = Log.objects.create(mailing=subject, user=mailing_object.users, responce_mailing='NO', responce_server=e)
        return log.save()
    finally:
        server.quit()

