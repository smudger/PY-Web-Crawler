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
MAX_THREADS = 8

queue = Queue()
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

# create worker threads (which die when main exits)
def create_workers():
    for _ in range(MAX_THREADS):
        thread = threading.Thread(target=work)
        thread.daemon = True
        thread.start()

# do next page in queue
def work():
    while True:
        url = queue.get()
        Spider.crawl(threading.current_thread().name, url)
        queue.task_done()

# each queued page is a job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# check if there are items in the queue and crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' pages in queue')
        create_jobs()

create_workers()
crawl()
