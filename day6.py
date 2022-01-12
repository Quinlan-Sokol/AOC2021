from collections import deque
lst = list(map(int, open("input6.txt", "r").readline().split(",")))

data = deque([lst.count(x) for x in range(9)])

for k in range(256):
    data[7] += data[0]
    data.rotate(-1)

print(sum(data))