N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()

ret = 0
l, r = 0, N-1

if l + r > 200000:
    print(0)
else:
    while l < r:
        if arr[l] + arr[r] < M:
            l += 1
        elif arr[l] + arr[r] == M:
            ret += 1
            r -= 1
        else:
            r -= 1

print(ret)