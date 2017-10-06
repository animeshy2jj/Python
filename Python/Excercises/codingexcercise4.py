def celtofah(celcius):
    if celcius<-273.15:
        return ("not possible")
    else:
        return (celcius*9/5+32)
#cel=float(input("Enter the temperatur on Degree Celcius :"))
temperatures=[10,-20,-289,100]
for temp in temperatures:
    print(celtofah(temp))
