a = iter(range(10))

print 'iterator has next: %s' % hasattr(a, 'next')

print a.next()  # 0
print a.next()  # 1
print a.next()  # 2

for n in a:
    print n  # calls a.next(), from 3 to 9


b = [100, 200, 300, 400, 500]
print 'list has an iterator: %s' % hasattr(b, '__iter__')

b_iter = b.__iter__()
print 'type of list iterator: %s' % type(b_iter)

print 'list iterator has next: %s' % hasattr(b_iter, 'next')

print b_iter.next()  # 100
print b_iter.next()  # 200
print b_iter.next()  # 300
print b_iter.next()  # 400
