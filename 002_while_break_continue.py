import random

menu = ['hamburguer', 'hot dog', 'broccoli', 'spaghetti', 'portuguese', ]

option = None

counter = 0
while option != 'broccoli':
    option = random.choice(menu)
    if option == 'broccoli':
        break
    counter += 1
    if option == 'portuguese':
        print '*** Are you crazy? "Portuguese" is not a valid option! ***'
        continue
    print('Thinking of %s...' % option)

print('After {0} tries, you chose {1}.'.format(counter, option))
print('Good choice!')
