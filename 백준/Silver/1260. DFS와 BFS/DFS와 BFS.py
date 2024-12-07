"""
1.전략
- DFS, BFS
- 인접 리스트 사용(sort 추가 필요)
- 정점(N), 간선(M), 시작점(V)이 주어질 때 방문 순회 원리 이해하기

2.시간 복잡도
- 시간 제한: 2초
- O(N+M) = 1,000 + 10,000 = 11,000
"""
from collections import deque
import sys
input = sys.stdin.readline

# Input
N, M, V = map(int, input().split())

# Variables
graph = {i:[] for i in range(N+1)}
visited1 = [False for _ in range(N+1)]
visited2 = [False for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for k in graph:
    graph[k].sort()

# Solution
def DFS(v: int):
    print(v, end=' ')
    visited1[v] = True
    
    for i in graph[v]:
        if not visited1[i]:
            DFS(i)

def BFS(v: int):
    q = deque()
    q.append(v)
    visited2[v] = True

    while q:
        x = q.popleft()
        print(x, end=' ')

        for i in graph[x]:
            if not visited2[i]:
                visited2[i] = True
                q.append(i)

# Main
DFS(V)
print()
BFS(V)