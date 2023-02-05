n = int(input())
a, cnt = 1, 1

while a < n:
    a += 6*cnt
    cnt += 1

print(cnt)