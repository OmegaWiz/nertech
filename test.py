import datetime
import datetime

d = datetime.date.today()

for i in range(1, 7):
    print(d + datetime.timedelta(days=i))

print(d)
