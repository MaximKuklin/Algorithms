import matplotlib.pyplot as plt
from random import randint

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def PP (arr):
    for i in arr:
        print('(', i.x, ',', i.y, ') ')

def pos(A, B, C):
    x = (B.x-A.x)*(C.y-B.y)-(B.y-A.y)*(C.x-B.x)
    return x

points = []

pointsx = []
pointsy = []

n = 1000

while (len(pointsx)!= n):
    x = randint(1, n*2)
    if x not in pointsx:
        pointsx.append(x)

while (len(pointsy) != n):
    y = randint(1, n*2)
    if y not in pointsy:
        pointsy.append(y)


print(pointsx, len(pointsx))
print(pointsy, len(pointsy))


for i in range(0, n):
    points.append(Point(pointsx[i], pointsy[i]))

n = len(points)-1
print (n)

p0 = Point(-100000, 100000)
for i in points:
    if i.y <= p0.y:
        p0.y = i.y
        p0.x = i.x

print (p0.x, p0.y)

index = 0
for i in points:
    if i.x == p0.x and i.y == p0.y:
        break
    else:
        index+=1

points[index], points[0] = points[0], points[index]

PP(points)
print ('\n')
for i in range(2, n):
    j = i
    while j > 1 and pos(p0, points[j-1], points[j]) < 0:
        points[j], points[j-1] = points[j-1], points[j]
        j -= 1

MBO = []
MBO.append(points[0])
MBO.append(points[1])

for i in range(2, n):
    while pos(MBO[-2], MBO[-1], points[i]) < 0:
        MBO.pop()
    MBO.append(points[i])

PP(MBO)

x1 = []
y1 = []

for i in MBO:
    x1.append(i.x)
    y1.append(i.y)

x1.append(MBO[0].x)
y1.append(MBO[0].y)


for i in points:
    plt.scatter(i.x, i.y)

plt.plot(x1, y1)
plt.show()
