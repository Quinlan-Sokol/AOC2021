from collections import Counter
with open("input5.txt", "r") as f:
    pipes = f.read().splitlines()

    c1 = Counter()
    c2 = Counter()
    for line in pipes:
        x1 = int(line.split(" -> ")[0].split(",")[0])
        y1 = int(line.split(" -> ")[0].split(",")[1])
        x2 = int(line.split(" -> ")[1].split(",")[0])
        y2 = int(line.split(" -> ")[1].split(",")[1])

        if x1 == x2:
            c1.update([(x1, min(y1, y2) + n) for n in range(abs(y1 - y2)+1)])
            c2.update([(x1, min(y1, y2) + n) for n in range(abs(y1 - y2)+1)])
        elif y1 == y2:
            c1.update([(min(x1, x2) + n, y1) for n in range(abs(x1 - x2)+1)])
            c2.update([(min(x1, x2) + n, y1) for n in range(abs(x1 - x2)+1)])
        else:
            xOff = int((x2-x1)/abs(x1-x2))
            yOff = int((y2-y1)/abs(y1-y2))
            c2.update([(x1 + xOff*n, y1 + yOff*n) for n in range(abs(x1 - x2)+1)])
    print("Part 1: " + str(len(list(filter(lambda x: x > 1, c1.values())))))
    print("Part 2: " + str(len(list(filter(lambda x: x > 1, c2.values())))))