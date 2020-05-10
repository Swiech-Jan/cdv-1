progr=['Python', 'PHP', 'C#', 'JS', 'Java']
print(progr)
print(type(progr))

first=progr[0]
print(first)

threeElements=progr[0:3]
print(threeElements)

last=progr[-1]
print(last)

#Dodanie nowego elementu na koniec listy
progr.append('R')
progr.append('Python')
print(progr)

#zliczanie lementu w liście
countElement=progr.count('Python')
print(countElement)

#Ilość elementów w liście 
countElementsOfList=len(progr)
print(countElementsOfList)

#Połączenie list
anotherList=['C', 'C++']
progr.extend(anotherList)
print('progr: ' + str(progr))
print('anotherList: ' + str(anotherList))

#Usuwanie elementów z listy
new=progr
print('New list:' + str(new))
new.clear()
print('New list:' + str(new))
print('Rozmiar New list: ' + str(len(new)))
print('progr list:' + str(progr))
print('Rozmiar progr list: ' + str(len(progr)))

x=8
print(x)
y=x
print(y)

y=5
print(x)  #8
print(y)  #5

'''
Dodaj listę o nazwie: country
Przypisz do niej 5 elementów
Poproś użytkownika, aby dodał dwa nowe elementy do listy
Uzytkownikowi wyświetl listę do wyboru:

1) Wyświetl pierwsze 3 elementy listy
2) Wyświetl elementy listy, które dodałem (dane pobierz z listy)
3) Wyświetl zawartość listy
4) Wyczyść zawartość listy
5) Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy)

Użytkownik raz dokonuje wyboru z listy.
Wyświetl zawartość listy po wykonaniu operacji przez użytkownika.
'''

