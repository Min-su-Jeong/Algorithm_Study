n = int(input())
p = list(map(int, input().split()))

res = 0
p.sort()
for i in range(1, n+1):
    res += sum(p[0:i])
print(res)