"""
1.전략
- BFS(Breath First Search)
- Screen, Clip, Time을 Queue에 넣어서 BFS를 진행
- Screen = S개가 되면 Time을 반환
- Screen < S이고 Screen이 Clip만큼 클립보드에 복사되어 있지 않으면 Screen을 Clip만큼 복사
- Screen > 0이면 Screen을 1개 삭제

2.시간복잡도
- 시간 제한: 2초
- O(N^2)
"""
import sys
from collections import deque
input = sys.stdin.readline

# Input
S = int(input())

# Variables
visited = [[0] * (S + 1) for _ in range(S + 1)]

# Solution
def bfs():
    q = deque()
    q.append((1, 0, 0))
    
    visited[1][0] = 1

    while q:
        screen, clip, time = q.popleft()

        if screen == S:
            return time

        if screen < S and not visited[screen][screen]:
            visited[screen][screen] = 1
            q.append((screen, screen, time + 1))

        if clip and screen + clip <= S and not visited[screen + clip][clip]:
            visited[screen + clip][clip] = 1
            q.append((screen + clip, clip, time + 1))

        if screen > 0 and not visited[screen - 1][clip]:
            visited[screen - 1][clip] = 1
            q.append((screen - 1, clip, time + 1))

# Output
print(bfs())