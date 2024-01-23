# acesta este un comentariu pe o linie
'''
comentarii multi line
linia 2
linia 3

'''
print('Salut Lume')  # comentariu

prima_variabila = 'prima mea variabila'
print(prima_variabila)

x, y, z = 'orange', 'banana', 'chery'
print(x, y)
a = b = c = 'apple'
print(b)

numar_intreg = 10
numar_real = 3.14
boolean = True  # False
null = None
print(30 * ' !')

# tipuri de  date

numar_intreg = 10  # variabila tip integer
numar_real = 3.14  # tip Float
boolean = True  # False  este o variabila tip Boolean
nume = 'Alin'  # este o variabila tip String

lista_numere = [1, 2, 3, 4]
lista_cuvinte = ['mere', 'pere', 'banane']
tuplu = (10, 20, 30)
dictionar = {'cheie1': 'valoare1', 'cheie1': 'valoare1'}

suma = numar_real + numar_intreg
print('suma este: ', suma)

# concatenarea 2 siruri
nume1 = 'Crina'
nume_complte = nume + ' Munteanu'
print('nemele complet este', nume_complte)

# test_variabila = nume1 + numar_intreg
# print(test_variabila)

print((30 * 5))
# functia Type
print('tipul de data al variabilei numar intreg ', type(numar_intreg))
print('tipul de data al variabilei numar real ', type(numar_real))
print('tipul de data al variabilei nume', type(nume1))
print('tipul de data al variabilei boolean ', type(boolean))
print('tipul de data al variabilei dictionar ', type(dictionar))
# fuctia Type Casting
# proces prin care se transforma o valoare de un tip in alt tip de date


numar_intreg1 = 18
numar_real1 = float(numar_intreg1)
print(numar_intreg1)
print(type(numar_real1))

test_variabila = nume1 + ' ' + str(numar_intreg)
print(test_variabila)

# inglobarea variabelelor in cadrul instructiunii Print
nume = 'Alina'
an_nastere = 1987
salariu = 5000.44

print(nume + 'este nascuta in anul' + str(an_nastere) + 'este angajat cu un salariu ' + str(salariu) + 'lei')
print(nume + 'este nascuta in anul' + str(an_nastere) + 'este angajat cu un salariu ' + str(salariu) + 'lei')
# printare cu formatare
print(f"{nume} este nascuta in anul {an_nastere} si este angajata cu salariul {salariu} lei")

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# Verifică tipul acesteia.
round(salariu)
print(round(5000.44))
# 6. Citește de la tastatură:
# numele;
# prenumele.
# Afișează: 'Numele complet are x caractere'
numele=input(f'Introduceti numele: ')
prenumele=input(f'Introduceti prenumele :')
numele_prenumele=input(f'Numele complet :')
print(f'{numele}{prenumele}')
print(f'{numele_prenumele}')
print(f'{numele_prenumele} are {len(numele_prenumele)} caractere')
# input este o fuctia predefinita care permita interactiunea utilizatorului prin citorea datelor de la tastatura
nume=input('Introdu nemele tau :')
print(f'Salut , {nume}')

# string methods- module pe care le vom importa
sir = 'Ana are mere'
print(sir)

sir2 = sir.replace('mere' ,'pere')
print(sir2)

sir_mere = sir.upper()
print(sir_mere)

sir_mic=sir.lower()
print(sir_mic)
sir_split =sir.split()
print(sir_split)

sir_index= sir.index('A')
print(sir_index)
sir_cap= sir.capitalize()
print(sir_cap)

lista=[1,2,3,4,6]
listanr=len(lista)
print(listanr)