import sys

ranges = sys.stdin.read().strip().split(",")

def repeating_any(num):
    for i in range(1, (len(num) // 2) + 1):
        if num[:i] * (len(num) // i) == num:
            return True
    return False

def repeating_twice(num):
    return num[:len(num)//2] == num[len(num)//2:]

p1 = 0
p2 = 0

for r in ranges:
    a,b = map(int, r.split("-"))
    for i in range(a,b+1):
        if repeating_twice(str(i)):
            p1 += i
        if repeating_any(str(i)):
            print(i)
            p2 += i
print(p1)
print(p2)
