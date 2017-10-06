def celtofah(celcius):
    if celcius<-273.15:
        return ("not possible")
    else:
        file.write(str(celcius*9/5+32) +"\n")
        
temperatures=[10,-20,-289,100]
with open("celcius.txt","w+") as file:
    for temp in temperatures:
        celtofah(temp)
