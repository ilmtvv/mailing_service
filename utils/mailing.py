from django.contrib.sites import requests
from django.core.mail import send_mail

from config import settings
from logs.models import Log

from utils.email_post import email_post


def mailing(mailing_object):

    #print(mailing_object)

    clients = mailing_object.clients.all()
    clients_list = []
    subject = mailing_object.message.title
    message = mailing_object.message.body

    for client in clients:
         clients_list.append(client.__str__())

    # print(clients_list)
    # print(subject)
    # print(message)

    mailing_object.mailing_status = 1
    mailing_object.save()


    email_post(subject, message, clients_list, mailing_object.users)

          # logs?
    # from_email = settings.EMAIL_HOST_USER
    # send_mail(subject, message, from_email, clients_list)
    #
    # log = Log.objects.create(mailing=subject, user=mailing_object.users, responce_mailing='OK', responce_server='OK')
    # log.save()
    clients_list = []
    mailing_object.mailing_status = -1  # три доступа к базе дынных в одной функции,
                                # не знаю как еще можно было бы контролировать статус рассылки
    mailing_object.save()