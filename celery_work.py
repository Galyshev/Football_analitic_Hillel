import os
from celery import Celery
from parser import parser

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
celery = Celery('celery_work', broker=f'pyamqp://guest@{rabbit_host}//')

@celery.task()
def data_update():
    # обновление данных
    parser.england_parser()
    parser.german_parser()
    parser.italy_parser()
    parser.statistics_parser()
    parser.spain_parser()
    parser.france_parser()





