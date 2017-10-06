names=['abc','def','ghi']
domains=['gmail','yahoo','outlook']
for i,j in zip(names,domains):
    print(i,j)
#even if we increase the size of one list... only 3 data lines will be printed
#does not matter if 'i' is before 'j' and vice-versa
