import random

places_to_eat = [
    'eskilos', 'cristovao', 'japanese', 'sativa', 'portuguese',
]

option = None

counter = 0
while option != 'eskilos':
    option = random.choice(places_to_eat)
    if option == 'eskilos':
        break
    counter += 1
    if option == 'portuguese':
        print 'Are you crazy? "Portuguese" is not a valid option!'
        continue
    print('Thinking of %s...' % option)

print('After {0} tries, you chose {1}.'.format(counter, option))
print('Good choice!')
