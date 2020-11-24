f = open('day1_input.txt', 'r')
line = f.readline()
floor = 0
i = 0
basement = 0


for c in line:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1

    i += 1
    if floor == -1 and basement == 0:
        basement = i

print(floor)
print(basement)