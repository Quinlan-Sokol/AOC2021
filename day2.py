with open("input2.txt", "r") as f:
    pos = 0
    depth = 0
    depth2 = 0
    aim = 0
    for line in f:
        if line.split()[0] == "forward":
            pos += int(line.split()[1])
            depth2 += int(line.split()[1]) * aim
        elif line.split()[0] == "down":
            depth += int(line.split()[1])
            aim += int(line.split()[1])
        elif line.split()[0] == "up":
            depth -= int(line.split()[1])
            aim -= int(line.split()[1])
    print(pos*depth)
    print(pos*depth2)