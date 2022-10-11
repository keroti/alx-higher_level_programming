#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    dividesum = 0
    for num in my_list:
        multiply = num[0] * num[1]
        sum += multiply
        dividesum += num[1]
    return sum / dividesum
