def print_params(*args, **kwargs):
    print '%s: %s' % (type(args), args)
    print '%s: %s' % (type(kwargs), kwargs)

print_params(1, 2, 3, foo='a', bar='2')
