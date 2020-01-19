# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5


def divisible_of_5(numbers_list):
    for number in numbers_list:
        if number % 5 == 0:
            print(number)


numbers_list = [5, 6, 2, 15, 234, 20, 17]
divisible_of_5(numbers_list)
