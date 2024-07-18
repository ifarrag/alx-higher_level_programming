#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    divide = 0
    for i in range(list_length):
            try:
                divide = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                divide = 0
            except TypeError:
                divide = 0
                print("wrong type")
            except IndexError:
                print("out of range")
                divide = 0
            finally:
                new_list.append(divide)
                continue
    return new_list
