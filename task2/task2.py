import sys
from fractions import Fraction
circleFile = sys.argv[1]
dotFile = sys.argv[2]
result = []
with open(circleFile, 'r') as circle:
    x, y = map(Fraction, circle.readline().split())
    r = Fraction(circle.readline())
with open(dotFile, 'r') as dots:
    i = 0# count lines < 100
    for line in dots:
        if i >= 100:
            break
        d_x, d_y = map(Fraction, line.split())
        num = (d_x - x) * (d_x - x) + (d_y - y) * (d_y - y) - r*r
        res = 0
        if (num < 0):
            res = 1
        elif (num > 0):
            res = 2
        result.append(res)
        i += 1
for e in result:
    print(e, end='\n')