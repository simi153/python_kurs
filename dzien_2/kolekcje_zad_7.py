licznik = 0
napis = input("Wprowadz jakis napis: ")
for litera in napis:
    if litera.lower() == "a" or litera == "e" or litera == "i" or litera == "o" or litera == "u" or litera == "y":
        licznik += 1
print("Liczba samoglosek: ", licznik)


licznik_2=0
samogloski="aeiouy"
for litera in napis:
    if litera.lower() in samogloski:
        licznik_2+=1
print("Liczba samoglosek: ", licznik_2)