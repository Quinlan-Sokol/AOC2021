lines = open("input10.txt", "r").read().splitlines()

dct1 = {")": 3,
       "]": 57,
       "}": 1197,
       ">": 25137}

dct2 = {"(": ")",
       "[": "]",
       "{": "}",
       "<": ">"}

dct3 = {")": 1,
       "]": 2,
       "}": 3,
       ">": 4}

t = 0
inc = []
for line in lines[::]:
    while any([x in line for x in ["()", "{}", "[]", "<>"]]):
        for b in ["()", "{}", "[]", "<>"]:
            line = line.replace(b, "")
    temp = list(filter(lambda x: x in ["}",")","]",">"], line))
    if len(temp) > 0:
        t += dct1[temp[0]]
    else:
        inc.append(line)
print("Part 1: " + str(t))


scores = []
for line in inc:
    ss = "".join([dct2[c] for c in line[::-1]])
    s = 0
    for c in ss:
        s = s*5 + dct3[c]
    scores.append(s)
print("Part 2: " + str(list(sorted(scores))[len(scores)//2]))