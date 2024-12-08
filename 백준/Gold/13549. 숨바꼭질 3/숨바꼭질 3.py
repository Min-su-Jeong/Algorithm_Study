"""
1.전략
- BFS(Breadth-First Search)
- 현재 점을 기준으로 X-1, X+1, 2*X의 위치를 방문하며 가장 빠른 시간 찾기
- X-1, X+1인 경우: 현재 점 배열의 값에서 + 1 / 아닌 경우: 현재 점 배열의 값

2.시간 복잡도
- 시간 제한: 2초
- O(N+K) = 100,000 + 100,000 = 200,000
"""
from collections import deque
import sys
input = sys.stdin.readline

# Input
N, K = map(int, input().split())

# Variables
MAX = 100001
pos = [0 for _ in range(MAX)]

# Solution
def BFS(x: int):
    q = deque([x])

    while q:
        x = q.popleft()

        if x == K:
            return pos[x]

        for nx in (x-1, x+1, x<<1):
            if 0 <= nx < MAX and not pos[nx]:
                if nx == x<<1 and nx != 0:
                    pos[nx] = pos[x]
                    q.appendleft(nx)
                else:
                    pos[nx] = pos[x] + 1
                    q.append(nx)
                    
# Main
print(BFS(N))