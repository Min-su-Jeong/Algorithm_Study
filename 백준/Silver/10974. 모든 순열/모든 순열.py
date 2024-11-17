"""
1.전략
- DFS(Depth-First Search)
- N만큼 반복하면서 중복 X인 순열 계산
- N의 길이에 도달할 때마다 출력

2.시간 복잡도
- 시간 제한: 1초
- O(N^N) = 8 * 8 = 64
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())

# Variables
arr = []
visited = [False for _ in range(N)]

# Solution
def dfs(curNum: int):
    if curNum == N:
        print(*arr)

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(i+1)
            dfs(curNum+1)
            visited[i] = False
            arr.pop()

# Main
dfs(0)