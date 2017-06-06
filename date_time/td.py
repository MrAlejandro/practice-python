import datetime
import time

now = datetime.datetime.now()
some_past_date = datetime.datetime(2017, 6, 5, 21, 11, 0, 333)
print(now, some_past_date)

delta = now - some_past_date
print(type(delta), delta, dir(delta))
print(delta.days, delta.seconds, delta.total_seconds())

def create_file(filename):
    with open(str(filename), 'w') as handler:
        handler.close()

filename = now.strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
print(filename)
# create_file(filename)

after_one_week = now + datetime.timedelta(days=7, seconds=7)
print(now, after_one_week)

lst = []

for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1) # the number is in seconds

print(lst)
