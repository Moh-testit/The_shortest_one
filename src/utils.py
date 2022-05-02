##
# EPITECH PROJECT, 2021
# B-MAT-500-COT-5-1-302separation-charmeel.vodouhe
# File description:
# utils
##

import os
import errors


def check_length(n):
    try:
        tmp = int(n)
        if (tmp <= 0):
            errors.report("max paths length must be strictly positive")
    except:
        errors.report("max paths length must be a number")
    return (tmp)
