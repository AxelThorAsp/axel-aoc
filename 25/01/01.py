import sys

lines = list(map(lambda x: x.replace('\n',''), sys.stdin.readlines()))

dial = 50
count_zero = 0

def do(rot):
    global dial
    global count_zero
    dir, deg = rot[0], int(rot[1:])
    if dial == 0:
        count_zero += 1
    assert deg in range(0,1001)
    if dir == 'R':
        dial = (dial + deg) % 100
    elif dir == 'L':
        dial = (dial - deg) % 100
    else:
        assert False

for l in lines:
    do(l)

print(count_zero)

