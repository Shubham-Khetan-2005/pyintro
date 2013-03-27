def sum(x, y):
    '''Returns the sum of two numbers'''
    return x + y


print help(sum)
print sum.__doc__

print sum(1, 2)


def welcome(name, greeting='hello'):
    print '%s %s, welcome!' % (greeting, name)


welcome('Peter')
welcome('Maria', 'hi there')
