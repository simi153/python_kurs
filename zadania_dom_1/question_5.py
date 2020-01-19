# Question 5: Given a list of ints, return True if first and last number of a list is same
def first_and_last(list):
    if list[0] == list[-1]:
        return True
    else:
        return False


simple_list = [2,3,6,-12,5,2,10,5]
print(first_and_last(simple_list))