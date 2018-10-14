import threading
from queue import Queue
from spider import Spider
from domain import *
from functions import *

PROJECT_NAME = 'bbc news'
HOME_PAGE = 'https://www.bbc.co.uk/news'
DOMAIN_NAME = get_subdomain_name(HOME_PAGE)
QUEUE_FILE = 'projects/' + PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = 'projects/' + PROJECT_NAME + '/crawled.txt'
MAX_THREADS = 4

queue = Queue()
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)
