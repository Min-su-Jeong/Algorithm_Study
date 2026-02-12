import sys
input = lambda: sys.stdin.readline().rstrip()

def check(s):
    return s == s[::-1]

N = int(input().strip())

ret = 0
strings = [input() for _ in range(N)]
for s in strings:
    if check(s):
        ret += 1

print(ret * (ret - 1))