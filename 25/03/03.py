import sys

banks = [list(map(int, list(l))) for l in sys.stdin.read().strip().split("\n")]

def max_jolt(bank):
    if len(bank) == 0:
        return 0
    mx = 0
    for i in range(1, len(bank)):
        n = bank[0]*10 + bank[i]
        if n > mx:
            mx = n
    return max(mx, max_jolt(bank[1:]))

s = sum([max_jolt(b) for b in banks])
print(s)
