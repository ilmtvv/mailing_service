from config import settings
from logs.models import Log

from utils.email_post import email_post


def mailing(mailing_object):

    clients = mailing_object.clients.all()
    subject = mailing_object.message.title
    message = mailing_object.message.body

    mailing_object.mailing_status = 1
    mailing_object.save()

    for client in clients:
        response_mailing, responce_server = email_post(subject, message,[client.email])
        log = Log.objects.create(mailing=subject, response_mailing=response_mailing, responce_server=responce_server)
        log.save()
        #   logs?


    mailing.mailing_status = 0  # три доступа к базе дынных в одной функции,
                                # не знаю как еще можно было бы контролировать статус рассылки
    mailing.save()