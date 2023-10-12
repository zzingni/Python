

import datetime

now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)


if now.hour < 12:
    print("오전")
else:
    print("오후")