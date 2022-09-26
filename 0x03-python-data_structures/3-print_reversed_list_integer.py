#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        reversed_list = []
        for value in my_list:
            reversed_list = [value] + reversed_list
        result = reversed_list[i]
        print("{:d}".format(result))
