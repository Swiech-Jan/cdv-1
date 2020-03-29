print("Anna")
print(8)

#potęgowanie
pow=2**10
print(pow)

text="CDV"
print(text*2)

#pobieranie danych z klawiatury
#  +  konkatenacja
name=input("Podaj imię:")
print("Twoje imię: " + name)

surname=input("Podaj swoje nazwisko:")
print("Imię: " + name + ", nazwisko: " + surname)

lengthName=str(len(name))
print("Długość imienia: " + lengthName)

lenSurname=len(surname)
print(lenSurname)
print(type(lenSurname))
print(type(lengthName))
print(type(surname))

'''
Użytkownik podaje z klawiatury swoje dane: imie, nazwisko, wiek,
wyświetl dane w formacie: 
Imie i nazwisko: ..., wiek: ... lat
'''
print("\nPodaj narodowość:", end="")
nationality=input()

surname="Kowalski"
firstLetter=surname[0]
print(firstLetter)
lastLetter=surname[len(surname)-1]
print(lastLetter)

#konwersja typów danych
a="10"
print(type(a))
a=int(a)
print(type(a))

b=6
print(type(b)) #int
b/=2 #b=b/2
print(type(b)) #float
print(b) #3.0

print()
surname="Nowakowski"
print(surname[0]) #N
print(surname[0:2]) #No
print(surname[-2]) #k
print(surname[-2:]) #ki
print(surname[:-2]) #Nowakows
print(surname[:-2:2]) #Nwkw