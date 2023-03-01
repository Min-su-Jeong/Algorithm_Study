from collections import deque

def bfs(x):
    q = deque([x])
    cnt, v[x] = 0, True
    while q:
        for nn in graph[q.popleft()]:
            if not v[nn]:
                v[nn] = True
                q.append(nn)
                cnt +=1
    return cnt

n = int(input()) # 컴퓨터의 수
m = int(input()) # 네트워크 쌍 개수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

v = [False for _ in range(n+1)]
print(bfs(1))