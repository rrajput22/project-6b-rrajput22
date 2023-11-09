# Author: Rajvi Rajput
# GitHub username: rrajput22
# Date: 11/08/2023
# Description: Recursive function named is_decreasing that takes as its parameter a list of numbers.
# It returns True if the elements of the list are decreasing but return False otherwise and assumes the array contains
# at least two elements


def is_decreasing(lst):
    """
    Recursive function to check if a list is strictly decreasing.
    """
    # Base  case to check if the list has one or zero elements and it is strictly decreasing
    if len(lst) <= 1:
        return True
    else:
        # Checks if the first element is greater than the second then continues with the rest of the list
        return lst[0] > lst[1] and is_decreasing(lst[1:])