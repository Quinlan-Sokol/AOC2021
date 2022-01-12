lst = list(map(int, open("input7.txt", "r").readline().split(",")))

print("Part 1: " + str(min([sum(map(lambda y: abs(x-y), lst)) for x in range(min(lst), max(lst)+1)])))
print("Part 2: " + str(min([sum(map(lambda y: (abs(x-y)*(abs(x-y)+1))/2, lst)) for x in range(min(lst), max(lst)+1)])))
