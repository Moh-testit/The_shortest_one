##
# EPITECH PROJECT, 2021
# B-MAT-500-COT-5-1-302separation-charmeel.vodouhe
# File description:
# errors
##

import sys


def report(msg):
    print(msg, file=sys.stderr)
    sys.exit(84)
