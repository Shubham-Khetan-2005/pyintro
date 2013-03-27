import datetime

today = datetime.date.today()
day = today.day

if day in range(1, 10):
    print('give me my payment!')
elif day == 11:
    print('out of money')
else:
    print('oh my God!')
