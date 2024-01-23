# 1
#  o variabiila este un container din memorie care stocheaza valori
# 2  Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
nume = 'Maria'  # String
numar_intreg = 8  # Intiger
numar_real = 8.16  # Float
boolean = True  # Boolean
# 3  Utilizează funcția type pentru a verifica dacă au tipul de date așteptat
print(type, nume)
print(type, numar_intreg)
print(type, numar_real)
print(type, boolean)
# 4  Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# Verifică tipul acesteia
numar_real = 8.16
print(f'{numar_real} rotunjit este  ', round(numar_real))
print(type, numar_real)
# 5 Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile
# Rezolvă nepotrivirile de tip prin ce modalitate dorești
print(f'{nume} invata programare')
print(f'Andrei are {numar_intreg} mere')
print(f'liniarul are  {numar_real} cm')
print(f'{nume} intra la ore la ora {numar_intreg} , dar intre tinp masoara un caiet care are {numar_real} cm ')
# 6 Citește de la tastatură:
# numele;
# prenumele.
# Afișează: 'Numele complet are x caractere'
numele=input('Introduceti numele:')
prenumele=input('Introduceti prenumele:')
print(f'Introduceti numele : {numele}')
nume_complet= f'{numele} {prenumele}'
lungime_nume=len(nume_complet)
print(f'numele comlpet este :{nume_complet}')
print(f'numele complet are {lungime_nume} de caractere')




