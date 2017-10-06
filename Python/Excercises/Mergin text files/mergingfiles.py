import datetime
with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt",'w') as filewrite:
    for i in range(1,4):
        with open("file"+str(i)+".txt",'r') as file:
            filewrite.write(file.read()+"\n")

#above code is hardcoded

#It can be written like this total_seconds
import glob2 #for file searching
import datetime

filenames=glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")
