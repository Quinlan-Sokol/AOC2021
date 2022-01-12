from math import prod
grid = list(map(lambda x: list(map(int, x)), open("input9.txt", "r").read().splitlines()))

t = 0
points = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if (y == 0 or grid[y-1][x] > grid[y][x]) and \
            (y == len(grid)-1 or grid[y+1][x] > grid[y][x]) and \
            (x == 0 or grid[y][x-1] > grid[y][x]) and \
            (x == len(grid[y])-1 or grid[y][x+1] > grid[y][x]):
            t += grid[y][x] + 1
            points.append((x,y))
print("Part 1: " + str(t))


def traverse(lst, x, y, visited):
    global grid
    if y != 0 and grid[y-1][x] != 9 and (x, y-1) not in visited:
        visited.append((x, y-1))
        lst[-1] += 1
        traverse(lst, x, y-1, visited)
    if y != len(grid)-1 and grid[y+1][x] != 9 and (x, y+1) not in visited:
        visited.append((x, y+1))
        lst[-1] += 1
        traverse(lst, x, y+1, visited)
    if x != 0 and grid[y][x-1] != 9 and (x-1, y) not in visited:
        visited.append((x-1, y))
        lst[-1] += 1
        traverse(lst, x-1, y, visited)
    if x != len(grid[y])-1 and grid[y][x+1] != 9 and (x+1, y) not in visited:
        visited.append((x+1, y))
        lst[-1] += 1
        traverse(lst, x+1, y, visited)


lst = []
for p in points:
    lst.append(1)
    traverse(lst, p[0], p[1], [p])

print("Part 2: " + str(prod(list(reversed(sorted(lst)))[0:3])))