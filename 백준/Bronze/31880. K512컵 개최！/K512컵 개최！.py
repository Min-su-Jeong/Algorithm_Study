N, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ret = 0
for i in a:
    ret += i

for i in b:
    if i == 0:
        continue
    ret *= i

print(ret)