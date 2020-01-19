# Question 9: Reverse a given number and return true if it is the same as the original number


def zamiana(liczba):
    liczba_1 = str(liczba)
    liczba_2 = liczba_1[::-1]

    if liczba_1 == liczba_2:
        return True
    else:
        return False


liczba = 1221
print(zamiana(liczba))
