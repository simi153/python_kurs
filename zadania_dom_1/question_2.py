# Question 2: Given a range of numbers.
# Iterate from o^th number to the end number and print the sum of the current number and previous number

def sum_in_range(user_range):
    previous_number = 0
    for i in range(user_range):
        sum_in_range = previous_number + i
        print(sum_in_range)
        previous_number = i


try:
    user_range = int(input("Podaj zakres sumowanych liczb: "))
    sum_in_range(user_range)

except ValueError:
    print("Nie podano liczby całkowitej!")
