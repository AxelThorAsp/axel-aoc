#!/usr/bin/env python3
import sys
from collections import defaultdict
from functools import cmp_to_key

r, l = sys.stdin.read().split("\n\n")

d = defaultdict(set)

def do(l):
    for i, c in enumerate(l):
        if not set(l[i+1:]) <= d[c]:
            return False
    return True

def sort(l):
    def compare(a, b):
        if (a in d[b]):
            return 1
        else: return -1
    return sorted(l, key=cmp_to_key(compare))

for rr in r.split("\n"):
    k,v = map(int, rr.split("|"))
    d[k].add(v)
c = 0
p2 = 0
for ll in l.strip().split("\n"):
    ls = list(map(int, ll.split(",")))
    if do(ls):
        c+=ls[len(ls)//2]
    else:
        ss = sort(ls)
        p2 += ss[len(ss)//2]

print(c)
print(p2)
