#!/usr/bin/env python3
##
# EPITECH PROJECT, 2021
# B-MAT-500-COT-5-1-302separation-charmeel.vodouhe
# File description:
# main
##

from os import name
import sys
import errors
import usage
import utils
from userClass import User


def checkArgs(ac, av):
    tab = []
    if ac == 2 and av[1] in ["-h", "--help"]:
        usage.display()
    if not (ac in [3, 4]):
        errors.report("Usage Error: try -h")
    try:
        with open(av[1], "r") as file:
            tab = file.readlines()
    except IOError:
        errors.report("Error file : " + av[1])
    if len(tab) == 0:
        errors.report("Empty file : " + av[1])
    if len(tab) >= 100:
        errors.report("Error file size : " + av[1])
    return tab


def friendshipLink(stmp, users):
    us1 = User(stmp[0])
    us2 = User(stmp[1])
    if not (us1 in users):
        users.append(us1)
    users[users.index(us1)].addContact(us2)
    if not (us2 in users):
        users.append(us2)
    users[users.index(us2)].addContact(us1)
    return (users)


def stockUsers(tab):
    users = []
    for connection in tab:
        tmp = connection.rstrip()
        stmp = tmp.split(" is friends with ")
        if (len(stmp) != 2 and tmp):
            errors.report("Friendship error")
        if (tmp):
            users = friendshipLink(stmp, users)
    return(users)


def theShortestPath(matrix, id1, id2, distance, currentPath):
    if (id1 == id2):
        return (distance)
    distance += 1
    newPath = []
    currentPath.append(id1)
    for i in range(len(matrix[id1])):
        if (matrix[id1][i]) and (i not in currentPath):
            newDistance = theShortestPath(
                matrix, i, id2, distance, currentPath.copy())
            if newDistance > 0:
                newPath.append(newDistance)
    if (len(newPath) == 0):
        return (-1)
    return min(newPath)


def adjMatrix(users):
    mat = []
    for i in range(len(users)):
        tmp = []
        for u in users:
            if (u in users[i].contactList):
                tmp.append(1)
            else:
                tmp.append(0)
        mat.append(tmp)
    return (mat)


def shortMatrix(matrix, maxDistance):
    sz = len(matrix)
    shMatrix = [[0 for _ in range(sz)] for _ in range(sz)]
    for i in range(sz):
        for j in range(i + 1, len(matrix)):
            distance = theShortestPath(matrix.copy(), i, j, 0, [])
            if distance > maxDistance or distance == -1:
                distance = 0
            shMatrix[i][j] = distance
            shMatrix[j][i] = distance
    return (shMatrix)


def display_matrix(mat):
    for a in mat:
        for i in range(len(a) - 1):
            print(a[i], end=" ")
        print(a[len(a) - 1])


def main(ac, av):
    sys.setrecursionlimit(2000)
    tab = checkArgs(ac, av)
    users = sorted(stockUsers(tab))
    mat = adjMatrix(users)
    if (len(av) == 3):
        mlength = utils.check_length(av[2])
        for u in users:
            print(u.name)
        print("")
        display_matrix(mat)
        print("")
        shmat = shortMatrix(mat, mlength)
        display_matrix(shmat)
    else:
        deg = 0
        us1 = User(av[2])
        us2 = User(av[3])
        if (us1 not in users) or (us2 not in users):
            deg = -1
        else:
            deg = theShortestPath(mat.copy(), users.index(
                us1), users.index(us2), 0, [])
        print("Degree of separation between " +
              av[2] + " and " + av[3] + ": ", end="")
        print(deg)


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
