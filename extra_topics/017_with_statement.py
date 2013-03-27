import time


class Timer:
    def __enter__(self):
        self.time = time.time()
        print 'Processing...'

    def __exit__(self, type, value, traceback):
        ellapsed = time.time() - self.time
        print 'Done in %s' % ellapsed

with Timer():
    for x in range(100000000L):
        pass
