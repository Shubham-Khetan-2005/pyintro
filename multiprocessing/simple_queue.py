import random
import logging
import threading
from Queue import Queue


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s | %(threadName)-10s | %(message)s'
)


class Producer(threading.Thread):
    def __init__(self, queue):
        super(Producer, self).__init__()
        self.queue = queue

    def run(self):
        for item in range(random.randint(5, 20)):
            logging.debug('producing %s' % item)
            self.queue.put(item)
        logging.debug('done')


class Consumer(threading.Thread):
    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            logging.debug('consuming %s' % item)
            self.queue.task_done()


queue = Queue()

producers = [Producer(queue) for x in range(10)]
consumers = [Consumer(queue) for x in range(5)]

counter = 1
for producer in producers:
    producer.setName('producer #%02d' % counter)
    producer.setDaemon(True)
    producer.start()
    counter += 1

counter = 1
for consumer in consumers:
    consumer.setName('consumer #%02d' % counter)
    consumer.setDaemon(True)
    consumer.start()
    counter += 1

for producer in producers:
    producer.join()

queue.join()

print 'Program terminated'
