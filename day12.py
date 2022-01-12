from collections import defaultdict

dct = defaultdict(list)
for line in open("input12.txt", "r").read().splitlines():
    dct[line.split("-")[0]].append(line.split("-")[1])
    if line.split("-")[0] != "start":
        dct[line.split("-")[1]].append(line.split("-")[0])

t = 0
def traverse1(visited, cur):
    global t
    if cur == "end":
        t += 1
    else:
        for c in [x for x in dct[cur] if x not in visited]:
            if c.isupper():
                traverse1(visited, c)
            else:
                traverse1(visited + [c], c)


paths = set()
def traverse2(visited, cur, b=True, lst=[]):
    lst.append(cur)
    global t
    global test
    if cur == "end":
        t += 1
        paths.add(",".join(lst))
    else:
        for c in dct[cur]:
            if c.isupper():
                traverse2(visited, c, b, lst[:])
            else:
                if b:
                    traverse2(visited + [c], c, False, lst[:])
                if c not in visited:
                    traverse2(visited + [c], c, b, lst[:])


traverse1(["start"], "start")
print(t)
traverse2(["start"], "start")
print(len(paths))