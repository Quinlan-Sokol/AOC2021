input = open("input17.txt", "r").readline()
minX = int(input.split(": ")[1].split(", ")[0].split("=")[1].split("..")[0])
maxX = int(input.split(": ")[1].split(", ")[0].split("=")[1].split("..")[1])
minY = int(input.split(": ")[1].split(", ")[1].split("=")[1].split("..")[0])
maxY = int(input.split(": ")[1].split(", ")[1].split("=")[1].split("..")[1])

c = 0
max = (0, -99, 0)
for xi in range(0, maxX+1):
    for yi in range(minY, abs(minY)+1):
        vx, vy = xi, yi
        cvx, cvy = vx, vy
        x,y = 0,0
        my = 0
        while True:
            x += vx
            y += vy
            if y > my:
                my = y

            if minX <= x <= maxX and minY <= y <= maxY:
                c += 1
                if my > max[2]:
                    max = (cvx, cvy, my)
                break

            if vx != 0:
                vx -= 1
            vy -= 1

            if x > maxX or y < minY:
                break

print(max)
print(c)