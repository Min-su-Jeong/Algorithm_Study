import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

MAX = 10001
adj = [[] for _ in range(MAX)]

def bfs(here):
    global visit_id

    visit_id += 1
    q = deque([here])
    visited[here] = visit_id
    cnt = 1

    while q:
        here = q.popleft()
        for there in adj[here]:
            if visited[there] == visit_id: 
                continue
            visited[there] = visit_id
            q.append(there)
            cnt += 1

    return cnt


if __name__ == "__main__":
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
        adj[b].append(a)

    mx = 0
    dp = [0] * MAX
    visited = [0] * MAX
    visit_id = 0
    for i in range(1, N+1):
        dp[i] = bfs(i)
        mx = max(mx, dp[i])

    for i in range(1, N+1):
        if dp[i] == mx:
            print(i, end=' ')
