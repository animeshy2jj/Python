import datetime
import time

lists=[]
for i in range(5):
    lists.append(datetime.datetime.now())
    time.sleep(2)#delays time (Seconds)

print(lists)
