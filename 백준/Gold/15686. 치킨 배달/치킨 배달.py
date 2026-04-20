N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

INF = 987654321
ret = INF
cList, hList = [], []
selectedChicken = []

def comb(idx: int, arr: list):
    if len(arr) == M:
        selectedChicken.append(arr[:])
        return
    
    for i in range(idx+1, len(cList)):
        arr.append(i)
        comb(i, arr)
        arr.pop()

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            hList.append((i, j))
        elif graph[i][j] == 2:
            cList.append((i, j))

comb(-1, [])

for ch in selectedChicken:
    total = 0
    for h in hList:
        mn = INF
        for i in ch:
            dist = abs(h[0] - cList[i][0]) + abs(h[1] - cList[i][1])
            mn = min(mn, dist)
        total += mn
    ret = min(ret, total)

print(ret)