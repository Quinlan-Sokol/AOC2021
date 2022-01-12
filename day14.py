from collections import Counter
template = "NNCB"
dct = dict()
for line in open("input14.txt", "r").read().splitlines():
    c1 = line.split(" -> ")[0][0]
    c2 = line.split(" -> ")[0][1]
    c3 = line.split(" -> ")[1]

    dct[c1+c2] = c1+c3+c2

for k in range(15):
    i = 0
    while i < len(template)-1:
        if template[i:i+2] in dct:
            template = template[:i] + dct[template[i:i+2]] + template[i+2:]
            i += 1
        i += 1
    counts = Counter(template)
    print(counts["N"], counts["C"], counts["B"], counts["H"])