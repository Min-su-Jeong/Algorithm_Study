import sys

input = sys.stdin.readline
lst = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    lst.append((x, y))

for c in lst: # 현재 사람
    rank = 1
    for n in lst: # 다음 사람
        if c[0] < n[0] and c[1] < n[1]:
            rank += 1 # 조건에 만족하면 등수가 밀려남
    print(rank, end=' ')