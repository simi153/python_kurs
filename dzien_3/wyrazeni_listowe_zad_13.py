zmienno_rzecinkowe = [el/10 for el in range(11)]
print(zmienno_rzecinkowe)

zbior_tupli={(el,el**2,el**3) for el in range(-10,10)}
print(zbior_tupli)
print()

napisy={"ala ma kota","kot ma ale","Jas ma psa"}
slownik = {el:len(el) for el in napisy}
print(slownik)