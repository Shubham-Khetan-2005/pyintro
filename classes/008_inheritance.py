class Hero:
    def __init__(self, name):
        self.name = name


class Cyclops(Hero):
    def optic_blast(self):
        print '%s is using optic blast...' % self.name


class Flash(Hero):
    def move_super_fast(self):
        print '%s is moving super fast...' % self.name


class SuperMan(Cyclops, Flash):
    def fly(self):
        print '%s is flying like a bird...' % self.name


hero = SuperMan('Clark Kent')
hero.optic_blast()
hero.move_super_fast()
hero.fly()
