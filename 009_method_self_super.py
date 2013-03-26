class Todo(object):
    def __init__(self, description, completed):
        self.description = description
        self.completed = completed

    def __str__(self):
        done = 'X' if self.completed else ' '
        return '[%s] %s' % (done, self.description)


class FancyTodo(Todo):
    def __str__(self):
        s = super(FancyTodo, self).__str__()
        return '%s\n%s\n%s' % ('=' * len(s), s, '-' * len(s))

todoList = []
todoList.append(Todo('Buy some coffee', True))
todoList.append(Todo('Make a lot of coffee', False))
todoList.append(Todo('Drink much more coffee', False))
todoList.append(FancyTodo('Lose weight', True))
todoList.append(FancyTodo('Eat less bacon', False))

for todo in todoList:
    print todo
