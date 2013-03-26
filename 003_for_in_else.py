import random

numbers = []
for x in range(10):
    numbers.append(random.randint(-3, 20))

for number in numbers:
    print 'Checking number: %d' % number
    if number < 0:
        raise ValueError('Invalid number!')
else:
    print 'You are lucky. All numbers are positive.'
