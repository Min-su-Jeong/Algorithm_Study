N = int(input())
M = int(input())
v = list(map(int, input().split()))
v.sort()

ret = 0
l, r = 0, N-1

if l + r > 200000:
    print(0)
else:
    while l < r:
        if v[l] + v[r] > M: 
            r -= 1
        elif v[l] + v[r] == M: 
            ret += 1
            r -= 1
        else: l += 1

    print(ret)