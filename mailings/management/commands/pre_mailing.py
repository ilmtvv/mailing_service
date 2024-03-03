import argparse
import sys

from django.core.management import BaseCommand

from mailings.models import Mailing
from utils.mailing import mailing


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--pk_mailing', type=int)

    def handle(self, *args, **options):

        pk_mailing = options['pk_mailing']

        mailing_object = Mailing.objects.get(pk=pk_mailing)

        mailing(mailing_object)