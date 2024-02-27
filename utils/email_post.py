from email.message import EmailMessage

from config import settings
import smtplib

def email_post(subject, message, recipient_list):   # проблемы с безопасностью
    from_email = settings.EMAIL_HOST_USER
    password_from_email = settings.EMAIL_HOST_PASSWORD

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject

    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.login(from_email, password_from_email)

    try:
        server.sendmail(from_email, recipient_list, msg.as_string())
        return True, 'sent'
    except Exception as e:
        return False, str(e)
    finally:
        server.quit()

