# Question 1: Accept two int values from the user and return their product.
# If the product is greater than 1000, then return their sum

def product(first_number, second_number):
    product = first_number * second_number
    if product > 1000:
        product = first_number + second_number
    return product


try:
    first_number = int(input("Podaj pierwsza liczbe: "))
    second_number = int(input("Podaj druga liczbe: "))

    print(product(first_number, second_number))
except ValueError:
    print("Nie wprowadzono liczby liczby calkowitej!")
