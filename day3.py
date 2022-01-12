from functools import reduce
from operator import add

with open("input3.txt", "r") as f:
    lst = list(map(lambda x : list(map(int, list(x))), f.read().splitlines()))
    gamma = list(map(lambda x : "1" if x > len(lst)/2 else "0", list(reduce(lambda x,y : map(add, x, y), lst))))
    epsilon = list(map(lambda x : "0" if x == "1" else "1", gamma))
    print(int("".join(gamma),2) * int("".join(epsilon), 2))

    ogr = list(range(len(lst)))
    i = 0
    while len(ogr) > 1:
        s = sum([lst[x][i] for x in ogr])
        if s >= len(ogr)/2:
            ogr = list(filter(lambda x : lst[x][i] == 1, ogr))
        else:
            ogr = list(filter(lambda x: lst[x][i] == 0, ogr))
        i += 1

    co2 = list(range(len(lst)))
    i = 0
    while len(co2) > 1:
        s = sum([lst[x][i] for x in co2])
        if s >= len(co2) / 2:
            co2 = list(filter(lambda x: lst[x][i] == 0, co2))
        else:
            co2 = list(filter(lambda x: lst[x][i] == 1, co2))
        i += 1

    print(int("".join(map(str, lst[ogr[0]])),2) * int("".join(map(str, lst[co2[0]])), 2))