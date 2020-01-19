# Question 4: Given a string and an int n, remove characters from string starting from zero up to n and return a new string

def remove(text, number):
    new_text = ""
    for index, value in enumerate(text):
        if index >= number:
            new_text += text[index]
    return new_text


try:
    text = input("Podaj przykladowy tekst: ")
    number = int(input("Ile znakow chcesz usunac?: "))

    print(remove(text, number))

except ValueError:
    print("Nie podano liczby, bądź liczba wieksza niz wielkosc tekstu!")
