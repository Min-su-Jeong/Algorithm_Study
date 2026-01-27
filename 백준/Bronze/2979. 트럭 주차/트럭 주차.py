A, B, C = map(int, input().split())

parking = [0] * 101
minNum = 101
maxNum = 0
ret = 0

for _ in range(3):
    s, e = map(int, input().split())
    minNum = min(minNum, s)
    maxNum = max(maxNum, e)

    for i in range(s, e):
        parking[i] += 1
        
for i in range(minNum, maxNum):
    if parking[i] == 1:
        ret += A
    elif parking[i] == 2:
        ret += 2 * B
    elif parking[i] == 3:
        ret += 3 * C

print(ret)