import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))
ms = 0 # 합의 최댓값

# 조합 이용
for c in combinations(cards, 3):
    if sum(c) <= m and sum(c) > ms:
        ms = sum(c)

print(ms)