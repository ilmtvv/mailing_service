import os
import sys
from datetime import datetime

from crontab import CronTab

from config.settings import BASE_DIR


def create_cron_jobs(object):
    cron = CronTab(user=True)

    path_to_python = sys.executable
    path_to_script = BASE_DIR / 'manage.py'


    command = f'{path_to_python} {path_to_script} pre_mailing --pk_mailing={object.pk}'

    job = cron.new(command=command)

    job.hour.on(object.mailing_time.hour)
    job.minute.on(object.mailing_time.minute)

    if object.periodicity == 'W':
        job.dow.on(datetime.now().weekday())

    if object.periodicity == 'M':
        job.day.on(datetime.now().day)

    job.set_comment(f'{object.pk}')
    cron.write()
