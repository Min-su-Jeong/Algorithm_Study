import sys
from itertools import combinations as c

n, k = map(int, sys.stdin.readline().split())
print(len(list(c(range(n), k))))