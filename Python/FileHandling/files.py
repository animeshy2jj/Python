file = open('example.txt','r')
content=file.read()
print(content)
content2=file.readlines()
print(content2)
#doesn't matter if it is a different variable...pointer moves for the file

#pointer back to starting position
file.seek(0)
content3=file.readlines()
print(content3)
content3=[i.rstrip("\n") for i in content3]
print(content3)
file.close()

#write
file = open('example1.txt','w')
file.write("this is a write example")
file.close()

#iterate and write
message = ["a","b","c"]
file=open("iteratewrite.txt",'w')
for msg in message:
    file.write(msg+("\n"))
file.close()

#appending
file = open("example1.txt",'a')
file.write("this is an apend mode")
file.close()

#WITH statement
with open("iteratewrite.txt",'a+') as file:
    file.seek(0)
    content=file.read()
    print(content)
    file.write("with statement demo")
    ontent=file.read()
    print(content)
#content will not get updated but the file will have the value

#r for reading only...file pointer placed at the beginning of the file.
#r+ bot read and write ...file pointer placed at the beginning of the file.
#w for writing only...overwrites the file and if file not present creates a new file
#w+ for reading and writing.....overwrites the file and if file not present creates a new file
#a for appending into a file... file pointer is at the end if the file if file exists...if does not exists then creates a new file
#a+ for appending and reading ...same as above
