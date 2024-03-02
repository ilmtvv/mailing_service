from crontab import CronTab

cron = CronTab(user=True)

for job in cron:
    print(job)
#
# cron.remove_all()
# cron.write()
