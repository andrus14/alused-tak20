import math

f = open('input.txt', 'r')

result = 0

for line in f.readlines():

    d = [int(el) for el in line.split('x')]
    areas = [d[0] * d[1], d[1] *d[2], d[0] * d[2]]
    result += 2 * sum(areas) + min(areas)

print(result)