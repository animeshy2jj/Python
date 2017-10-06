listwa=['1',2,'3',4]
for item in listwa:
    print (item)

listpart2=['abc','def','abcxyz','defxyz']
for item in listpart2:
    if 'xyz' in item:
        print (item)

listpart3=["abc"]
for item in listpart3:
    print(item)

listpart4=["Terribly Tricky"]
for word in listpart4:
    for letter in word[-6:]:
        print(letter)
