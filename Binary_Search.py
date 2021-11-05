# -*- coding: utf-8 -*-

def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False

    mid = (low + high) / 2

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)
