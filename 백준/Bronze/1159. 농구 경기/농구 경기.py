N = int(input())

player = {}
for _ in range(N):
    s = input()[0]
    player[s] = player.get(s, 0) + 1

ret = ''
for k, v in sorted(player.items()):
    if v >= 5:
        ret += k

if ret:
    print(ret)
else:
    print("PREDAJA")