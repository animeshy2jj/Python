import datetime

filemname=datetime.datetime.now()

def create_file():
    with open(filemname.strftime("%Y-%m-%d-%H-%M-%S-%f"),'w') as file:#+(".txt")
        file.write("")
create_file()
