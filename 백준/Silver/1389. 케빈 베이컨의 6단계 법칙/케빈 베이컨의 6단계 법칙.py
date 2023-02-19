import sys
from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        target = queue.popleft()
        for i in graph[target]: # 탐색하지 않은 친구라면 탐색
            if not visited[i]:
                visited[i] = visited[target] + 1 # 탐색하기 위한 횟수 체크
                queue.append(i)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

kb = [] # 케빈 베이컨
for i in range(1, n + 1): # 모든 친구 탐색
    visited = [0] * (n + 1)
    bfs(i)
    kb.append(sum(visited))

print(kb.index(min(kb)) + 1)