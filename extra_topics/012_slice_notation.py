#  +---+---+---+---+---+---+---+---+---+---+---+
#  | H | e | l | l | o |   | W | o | r | l | d |
#  +---+---+---+---+---+---+---+---+---+---+---+
#    0   1   2   3   4   5   6   7   8   9  10   # offset from start
#  -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   # offset from end

s = 'Hello World'

print s[0]          # H
print s[-11]        # H
print s[1]          # e

print s[-1]         # d
print s[-2]         # l

print s[0:5]        # Hello
print s[6:]         # World
print s[:-6]        # Hello

print s[::-1]       # dlroW olleH
