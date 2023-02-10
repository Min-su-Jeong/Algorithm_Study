from itertools import combinations as c

n, k = map(int, input().split())
print(len(list(c(range(n), k))))