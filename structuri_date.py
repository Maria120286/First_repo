# listele in python pot sa cuprinda elemente de tipuri diferite
# au dimensiune dinamica
fructe =['mar , banana, portocala , 3, True  ']


# afisam o lista
print(fructe)

# accesam un element in functie de index

# adaugam un nou element
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'para'

#afisam lista
print(fructe)
# aflam dimensiunea
print(len(fructe))
# scoate si ne returneaza ultimul element
last = fructe.pop()
print(last)
print(fructe)
# de cate ori apare un element
print(fructe.count(0))
#extindem lista
fructe_exotice = ['ananas' , 'kivi']
fructe.extend(fructe_exotice)
print(fructe)





