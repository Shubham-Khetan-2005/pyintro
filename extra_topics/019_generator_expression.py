g = (x ** x for x in range(5))

print 'type of g: %s' % type(g)

print 'g has next: %s' % hasattr(g, 'next')

print g.next()  # 0**0 = 1
print g.next()  # 1**1 = 1
print g.next()  # 2**2 = 4
print g.next()  # 3**3 = 9

print 'generator has an iterator: %s' % hasattr(g, '__iter__')

g_iter = g.__iter__()
print 'type of generator iterator: %s' % type(g_iter)

print 'generator iterator has next: %s' % hasattr(g_iter, 'next')

print g_iter.next()  # 4**4 = 256
