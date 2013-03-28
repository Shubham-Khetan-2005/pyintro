import random


def random_generator(n):
    c = 0
    print 'before while'
    while c < n:
        print '\tbefore yield'
        yield random.randint(1, 1000)
        print '\tafter yield'
        c += 1
    print 'after while'

print 'type of random_generator: %s' % type(random_generator)

rg3 = random_generator(3)
print 'type of random_generator(3): %s' % type(rg3)

for r in rg3:
    print '\t\tinside for-loop: %s' % r
