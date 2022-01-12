from itertools import chain

grid = [list(map(int, x)) for x in open("input11.txt", "r").read().splitlines()]
flashes = 0


def simFlash(x, y):
    grid[x][y] = -1
    for dir in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
        if 0 <= x + dir[0] < 10 and 0 <= y + dir[1] < 10:
            if grid[x+dir[0]][y+dir[1]] != -1:
                grid[x+dir[0]][y+dir[1]] += 1

    for dir in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
        if 0 <= x + dir[0] < 10 and 0 <= y + dir[1] < 10:
            if grid[x + dir[0]][y + dir[1]] > 9:
                simFlash(x + dir[0], y + dir[1])


k = 0
while True:
    k += 1
    #if k < 5:
    #    print("\n".join(["".join(map(str, x)) for x in grid]) + "\n")
    for i in range(10):
        for j in range(10):
            grid[j][i] += 1

    for i in range(10):
        for j in range(10):
            if grid[j][i] > 9:
                simFlash(j, i)

    for i in range(10):
        for j in range(10):
            if grid[j][i] <= -1:
                flashes += 1
                grid[j][i] = 0

    if k == 100:
        print("Part 1: " + str(flashes) + " Flashes")

    if sum(chain(*grid)) == 0:
        print("Part 2: Step " + str(k))
        break