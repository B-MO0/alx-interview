#!/usr/bin/python3
"""Function that rotates 2D matrix"""


def rotate_2d_matrix(matrix):
    """ Rotate 2D matrix in place by 90 degrees """
    # * pass all items in list to operation
    # so zip(*matrix) is the same as zip(matrix[0], matrix[1], ...)
    # zip makes a list of tuples from the list of lists
    # And then convert the list of tuples to a list of lists
    # :: is normal slice operator with step to move elements to previous
    matrix[:] = [list(i) for i in zip(*matrix[::-1])]
