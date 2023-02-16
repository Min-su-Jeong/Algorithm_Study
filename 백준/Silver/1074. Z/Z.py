import sys
n, r, c = map(int, sys.stdin.readline().split())
visit = 0

while n > 1:
    size = (2**n) // 2
    if r < size and c >= size: # 2사분면
        visit += size ** 2
        c -= size
    elif r >= size and c < size: # 3사분면
        visit += size ** 2 * 2
        r -= size
    elif r >= size and c >= size: # 4사분면
        visit += size ** 2 * 3
        r -= size
        c -= size
    n -= 1

if (r,c) == (0,0):
    print(visit)
elif (r,c) == (0,1):
    print(visit+1)
elif (r,c) == (1,0):
    print(visit+2)
else:
    print(visit+3)