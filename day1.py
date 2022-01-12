
with open("input1.txt", "r") as f:
    lst = f.readlines()
    prev = int(lst[0])
    c = 0
    for line in lst[1::]:
        if int(line) > prev:
            c += 1
        prev = int(line)
    print(c)

    c = 0
    win = list(map(int, lst[0:3]))
    for i in range(1, len(lst)-2):
        if sum(map(int, lst[i:i+3])) > sum(win):
            c += 1
        win = map(int, lst[i:i+3])
    print(c)