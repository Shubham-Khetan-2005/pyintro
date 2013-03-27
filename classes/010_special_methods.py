def explore(obj):
    cls = obj.__class__
    name = cls.__name__
    members = cls.__dict__.items()

    print 'class %s(object):' % name
    for name, value in members:
        if not name.startswith('__'):
            if hasattr(value, '__call__'):
                print '\tdef %s(): pass' % name
            else:
                print '\t%s = %s' % (name, value)


class Foo(object):
    bar = 123
    xpto = 'abc'

    def baz(self):
        pass


explore(Foo())
