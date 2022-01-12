from collections import defaultdict, Counter

with open("input8.txt", "r") as f:
    t = 0

    numbers = {0: set(["a","b","c","e","f","g"]),
               1: set(["c","f"]),
               2: set(["a","c","d","e","g"]),
               3: set(["a","c","d","f","g"]),
               4: set(["b","c","d","f"]),
               5: set(["a","b","d","f","g"]),
               6: set(["a","b","d","e","f","g"]),
               7: set(["a","c","f"]),
               8: set(["a","b","c","d","e","f","g"]),
               9: set(["a","b","c","d","f","g"]),}

    for line in f.read().splitlines():
        patterns = ["".join(sorted(x)) for x in line.split(" | ")[0].split()]
        output = ["".join(sorted(x)) for x in line.split(" | ")[1].split()]

        mapping = dict()
        i = 0
        while i < len(patterns):
            if len(patterns[i]) == 2:
                mapping[patterns[i]] = 1
                mapping[1] = patterns[i]
                patterns.pop(i)
                i -= 1
            elif len(patterns[i]) == 3:
                mapping[patterns[i]] = 7
                mapping[7] = patterns[i]
                patterns.pop(i)
                i -= 1
            elif len(patterns[i]) == 4:
                mapping[patterns[i]] = 4
                mapping[4] = patterns[i]
                patterns.pop(i)
                i -= 1
            elif len(patterns[i]) == 7:
                mapping[patterns[i]] = 8
                mapping[8] = patterns[i]
                patterns.pop(i)
                i -= 1
            i += 1

        for p in patterns:
            if len(p) == 5 and all([c in p for c in mapping[1]]):
                mapping[p] = 3
                mapping[3] = p
                patterns.remove(p)

        for p in patterns:
            if len(p) == 6 and all([c in p for c in mapping[4]]):
                mapping[p] = 9
                mapping[9] = p
                patterns.remove(p)

        for p in patterns:
            if len(p) == 6 and all([c in p for c in mapping[7]]):
                mapping[p] = 0
                mapping[0] = p
                patterns.remove(p)

        for p in patterns:
            if len(p) == 6:
                mapping[p] = 6
                mapping[6] = p
                patterns.remove(p)

        for p in patterns:
            if len(p) == 5 and all([c in mapping[6] for c in p]):
                mapping[p] = 5
                mapping[5] = p
                patterns.remove(p)

        for p in patterns:
            if len(p) == 5:
                mapping[p] = 2
                mapping[2] = p
                patterns.remove(p)

        t += int("".join(map(lambda x: str(mapping[x]), output)))
    print(t)