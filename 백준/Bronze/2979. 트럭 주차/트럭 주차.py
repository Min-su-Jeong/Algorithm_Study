A, B, C = map(int, input().split())

mp = {}
ret = 0

for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        mp[i] = mp.get(i, 0) + 1

for v in mp.values():
    if v == 1: ret += A
    elif v == 2: ret += 2 * B
    elif v == 3: ret += 3 * C

print(ret)