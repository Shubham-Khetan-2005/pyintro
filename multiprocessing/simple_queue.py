import threading
from Queue import Queue
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s | %(threadName)-10s | %(message)s'
)


class Producer(threading.Thread):
    def __init__(self, queue):
        super(Producer, self).__init__()
        self.queue = queue

    def run(self):
        for x in range(100):
            logging.debug('%s producing %s' % (self.getName(), x))
            self.queue.put(x)
        logging.debug('%s done' % self.getName())


class Consumer(threading.Thread):
    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            logging.debug('%s consuming %s' % (self.getName(), item))
            self.queue.task_done()


queue = Queue()

producers = [Producer(queue) for x in range(2)]
consumers = [Consumer(queue) for x in range(6)]

counter = 1
for producer in producers:
    producer.setDaemon(True)
    producer.start()

for consumer in consumers:
    consumer.setDaemon(True)
    consumer.start()

queue.join()

print 'Program terminated'
