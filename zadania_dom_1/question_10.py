# Question 10: Given a two list of ints create a third list such that should contain only odd numbers from the first list and even numbers from the second list


def merge(list_1,list_2):
    merged = []
    for number in list_1:
        if number %2 !=0:
            merged.append(number)
    for number in list_2:
        if number%2==0:
            merged.append(number)
    return merged

list_1=[10, 20, 23, 11, 17]
list_2=[13, 43, 24, 36, 12]
print(merge(list_1,list_2))