import sys

grid = sys.stdin.read().strip().split('\n')

dirs = [
    (1,  0),
    (-1, 0),
    (0,  1),
    (0, -1),
    (1,  1),
    (-1, -1),
    (1, -1),
    (-1, 1)
]

def ok(y, x):
    notat = 0
    for dy, dx in dirs:
        if y + dy < 0 or y + dy >= len(grid) or x + dx < 0 or x + dx >= len(grid[0]):
            notat += 1
        elif grid[y + dy][x + dx] != "@":
            notat += 1
    return notat > 4



xs = 0
for j in range(len(grid)):
    for i in range(len(grid[0])):
        if grid[j][i] == "@" and ok(j,i):
            xs += 1
print(xs)
