def celtofah(celcius):
    if celcius<-273.15:
        return ("not possible")
    else:
        return (celcius*9/5+32)
cel=float(input("Enter the temperatur on Degree Celcius :"))
print(celtofah(cel))
