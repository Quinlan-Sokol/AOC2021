import math
from itertools import chain


def checkNum(grid, n):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == n:
                grid[i][j] = -1


def hasWon(grid, n):
    valid = any([row.count(-1) == 5 for row in grid]) or any([row.count(-1) == 5 for row in zip(*grid[::-1])])
    if valid:
        return n * sum([x for x in chain(*grid) if x != -1])
    return -1


with open("input4.txt", "r") as f:
    lst = list(map(int, f.readline().split(",")))

    temp = [x.strip("\n").strip(" ") for x in f.readlines() if x != "\n"]

    grids = [[[y for y in range(5)] for x in range(5)] for k in range(int(len(temp)/5))]

    for i in range(len(temp)):
        grids[math.floor(i/5)][i%5] = list(map(int, temp[i].split()))

    b = False
    for n in lst:
        i = 0
        while i < len(grids):
            checkNum(grids[i], n)

            r = hasWon(grids[i], n)
            if r != -1:
                if not b:
                    b = True
                    print("Part 1: " + str(r))
                if len(grids) == 1:
                    print("Part 2: " + str(r))
                grids.pop(i)
                i -= 1
            i += 1
        else:
            continue
        break
