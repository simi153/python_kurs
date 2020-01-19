import datetime


try:
    rok_urodzenia = int(input("Podaj rok urodzenia:"))
    if rok_urodzenia >0 and rok_urodzenia < 2020:
        if datetime.datetime.now().year-rok_urodzenia >= 18 :
            print("Jesteś pełnoletni")
        else:
            print("Nie jestes pelnoletni")
    else:
        print("Rok urodzenia musi sie miescic w przedziale 1-2019!")
except:
    print("Wprowadziles bledny rok urodzenia!")