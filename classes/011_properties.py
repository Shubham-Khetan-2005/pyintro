class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @name.setter
    def name(self, value):
        s = value.split()
        self.first_name = s[0]
        self.last_name = ' '.join(s[1:])


john = Person('John', 'Smith')
print john.name

john.name = 'John Brown Smith'
print john.name
