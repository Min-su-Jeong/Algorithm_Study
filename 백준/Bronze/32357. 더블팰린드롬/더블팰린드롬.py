import sys
input = sys.stdin.readline

def check(s):
    return s == s[::-1]

N = int(input().strip())
ret = 0

strings = []
for _ in range(N):
    s = input().strip()
    strings.append(s)

for s in strings:
    if check(s):
        ret += 1

print(ret * (ret - 1))