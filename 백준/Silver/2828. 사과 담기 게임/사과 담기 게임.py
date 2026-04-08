N, M = map(int, input().split())
J = int(input())

ret = 0
l, r = 1, 1

for _ in range(J):
    r = l + M - 1

    pos = int(input())
    if l <= pos <= r:
        continue

    if pos < l:
        ret += (l - pos)
        l = pos
    elif pos > r:
        ret += (pos - r)
        l += (pos - r)

print(ret)