"""
1.전략
- BFS(Breadth-First Search)
- 덱(Deque)을 사용해서 수빈이의 위치를 기준으로 X-1, X+1, 2*X의 위치를 순회

2.시간 복잡도
- 시간 제한: 2초
- O(N) = 100,000 * 3 = 300,000
"""
from collections import deque
import sys
input = sys.stdin.readline

# Input
N, K = map(int, input().split())

# Variables
MAX = 100001
arr = [0 for _ in range(MAX)]

# Solution
def bfs(x: int):
    q = deque([x])

    while q:
        x = q.popleft()
        
        if x == K:
            return arr[x]
        
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < MAX and not arr[nx]:
                arr[nx] = arr[x] + 1
                q.append(nx)

# Main
res = bfs(N)

# Output
print(res)