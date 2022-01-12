from functools import reduce

points = set()
folds = []

for line in open("input13.txt", "r").read().splitlines():
    if "," in line:
        points.add((int(line.split(",")[0]), int(line.split(",")[1])))
    elif "fold" in line:
        folds.append((0 if "x" in line else 1, int(line.split()[2].split("=")[1])))

for k, fold in enumerate(folds):
    lst = set([p for p in points if p[fold[0]] > fold[1]])
    points -= lst
    lst = list(map(list, lst))
    for p in lst:
        p[fold[0]] = 2*fold[1] - p[fold[0]]
        points.add(tuple(p))
    print("Fold " + str(k+1) + ": " + str(len(points)))

maxX = reduce(lambda x,y: x if x[0] > y[0] else y, points)[0]
maxY = reduce(lambda x,y: x if x[1] > y[1] else y, points)[0]
grid = [["#" if (x, y) in points else "." for y in range(maxY)] for x in range(maxX)]

print("\n".join(["".join(x) for x in zip(*grid)]))