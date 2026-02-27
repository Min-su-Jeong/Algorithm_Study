import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mp = {}
for _ in range(N):
    for x in map(int, input().split()):
        mp[x] = mp.get(x, 0) + 1

odd = sum(v & 1 for v in mp.values())

if M == 1:
    print("YES")
elif M % 2 == 0:
    if odd == 0:
        print("YES")
    else:
        print("NO")
else:
    if odd <= N and (N - odd) % 2 == 0:
        print("YES")
    else:
        print("NO")