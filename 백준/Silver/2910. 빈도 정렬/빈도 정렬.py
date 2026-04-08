N, C = map(int, input().split())
msg = list(map(int, input().split()))

freq, idx = {}, {}
for i, m in enumerate(msg):
    freq[m] = freq.get(m, 0) + 1
    if m not in idx:
        idx[m] = i

v = list(freq.keys())
v.sort(key=lambda x: (-freq[x], idx[x]))

for i in v:
    print(f"{i} " * freq[i], end='')