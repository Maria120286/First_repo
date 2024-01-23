# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
list3 = list_1 + list_2
print(list3)
for x in list_2:
    list_1.append(x)
    print(list_1)
    # 4.
    # Sortează și afișează lista generată la exercițiul anterior.
    # Sortează numărul 0 folosind o funcție.
    # Afișaza iar lista.
    # list3.extend(0)
    print(list3)
    # 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# Lista este goală.
# Lista nu este goală.
if list3 == list:
    print(f'lista este goala')
else:
    print(f'lista nu este goala')
    # 6. Folosește o funcție care să șteargă lista de la exercițiul 3
# list3.clear()
# print(list3)
# Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
if list3.clear():
    print(f'lista este goala')
else:
    print(f'lista nu este goala')
print(list3)
# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
x = dict1.keys()
print(x)
# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
print(x)
for x in dict1.values():
   print(x)
   #10. Dorel a făcut contestație și a primit 6
#Modifică nota lui Dorel în 6
#Printează nota după modificare
dict1.pop('Dorel')
print(dict1)
dict1[' Dorel']=6
print(dict1)
#11. Gigel se transferă din clasă
#căuta o funcție care să îl șteargă
#Vine un coleg nou. Adaugă Ionică, cu nota 9
#Printează noii elevi
dict1.pop('Gigel')
print(dict1)
dict1['Ionica']=9
print(dict1)
# 13.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# Adaugă în zilele_sapt ‘luni’
# Afișează zile_sapt
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
print(zile_sapt)
#14.Folosește un if și verifică dacă:
#Weekend este un subset al zilelor din săptămânii.
#Weekend nu este un subset al zilelor din săptămânii.

if zile_sapt == weekend:
    print(f'este un sebset')
else:
    print(f'nu este un subset')
    #15. Afișează diferențele dintre aceste 2 seturi.

# Afișează intersecția elementelor din aceste 2 seturi

