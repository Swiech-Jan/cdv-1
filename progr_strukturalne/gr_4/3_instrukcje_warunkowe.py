x=6

if x==5:
  print("x jest równa 5")
else:
  print("x nie jest równy 5")
  print("x jest równy: " + str(x))

print("Koniec instrukcji warunkowej")

######################################

y=False
if y:
  print("Prawda")
else:
  print("Fałsz")

######################################

z = 5 > 6
if z:
  print("Prawda")
else:
  print("Fałsz")

'''
Użytkownik podaje wartości trzech zmiennych: x, y, z
Wyświetl, która z tych wartości będzie największa,
wykorzystaj instrukcję warunkową
'''

x=input("Podaj x:")
y=input("Podaj y:")
z=input("Podaj z:")

if x >= y and x >= z:
  print('Wartość ' + x + ' jest największa')
elif y >= x and y >= z:
  print('Wartość ' + y + ' jest największa')
else:
  print('Wartość ' + z + ' jest największa')