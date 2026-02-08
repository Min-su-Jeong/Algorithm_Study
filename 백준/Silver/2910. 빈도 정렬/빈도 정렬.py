import sys
input = lambda: sys.stdin.readline().rstrip()

N, C = map(int, input().split())
arr = list(map(int, input().split()))

idx = {}
freq = {}
for i, x in enumerate(arr):
    freq[x] = freq.get(x, 0) + 1
    if x not in idx:
        idx[x] = i

v = list(freq.keys())

v.sort(key=lambda x: (-freq[x], idx[x]))

for i in v:
    print(f"{i} " * freq[i], end='')