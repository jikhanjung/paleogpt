from multiprocessing.spawn import prepare
from unittest import runner
from chat.models import CollectionCache, ItemCache, CollectionItemRel, LastVersion
from django.core.management.base import BaseCommand
import subprocess
from django.conf import settings
import os, shutil, sys
import time, datetime
from django.utils import timezone
import signal
import io
from chat.ZWrapper import ZWrapper

class Command(BaseCommand):
    help = "Customized load data for DB migration"
    runner = None

    def add_arguments(self , parser):
        parser.add_argument('zotero_user_id' , help='zotero_user_id')
        parser.add_argument('zotero_api_key', help='zotero_api_key')
        
    def handle(self, **options):
        print(options)
        #event_ids =  kwargs['event_id']
        zotero_user_id = options['zotero_user_id']
        zotero_api_key = options['zotero_api_key']

        z = ZWrapper(zotero_user_id, zotero_api_key)
        z.build_database()