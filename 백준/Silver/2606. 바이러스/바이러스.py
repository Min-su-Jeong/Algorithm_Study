import sys
from collections import deque

def dfs(x):
    v[x] = True
    for nn in graph[x]:
        if v[nn] == False:
            dfs(nn)

input = sys.stdin.readline
n = int(input()) # 컴퓨터의 수
m = int(input()) # 네트워크 쌍 개수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

v = [False for _ in range(n+1)]
dfs(1)
print(sum(v)-1)