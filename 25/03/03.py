import sys

banks = [list(map(int, list(l))) for l in sys.stdin.read().strip().split("\n")]

dp = {}
def _help(bank, index, picked, num_len):
    if picked == num_len:
        return 0
    if len(bank) == index and picked < num_len:
        return -10**20
    k = (hash(tuple(bank)), index, picked, num_len)
    if k in dp:
        return dp[k]
    ans = _help(bank, index + 1, picked, num_len)
    dp[k] = ans
    if picked < num_len:
        ans = max(ans, 10**((num_len - 1) - picked) * bank[index] + _help(bank, index + 1, picked + 1, num_len))
        dp[k] = ans
    return ans

def p1():
    return sum((_help(b, 0, 0, 2) for b in banks))

def p2():
    return sum((_help(b, 0, 0, 12) for b in banks))

print(p1())
print(p2())
