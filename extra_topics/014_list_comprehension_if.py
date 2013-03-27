numbers = [-3, 8, 56, -77, 100, -1, 5]
print 'All: %s' % numbers

positive = [number for number in numbers if number > 0]
print 'Positive: %s' % positive

negative = [number for number in numbers if number < 0]
print 'Negative: %s' % negative
