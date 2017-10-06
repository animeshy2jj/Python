#import datetimewa ---->importing this means you are running the imported class
import datetime
print(datetime.datetime.now())
yest = datetime.datetime(12,12,12,12,12,12,12)
now=datetime.datetime.now()
difference = now-yest
print(difference.days)
print(difference.total_seconds())
print(type(difference))

#adding days
alter=now+datetime.timedelta(days=2)
print(now)
print(alter)
