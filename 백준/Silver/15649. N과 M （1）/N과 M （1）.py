"""
1.전략
- 백트래킹(Back Tracking)
- list를 한 개 만들어 관리. DFS + 가지치기 추가
- 순열 내에 숫자가 중복될 수 없도록 구현

2.시간 복잡도
- 시간 제한: 1초
- O(N^2) = 8 * 8 = 64
"""
import sys
input = sys.stdin.readline

# Input
N, M = map(int, input().split())

# Variable
graph = [i for i in range(1, N+1)]
visited = [False for _ in range(N+1)]
arr = []

# Function
def dfs(curNum: int):
    global arr

    # 종료 조건
    if curNum == M:
        print(*arr)
        return

    # 방문 조건
    for j in range(1, N+1):
        if not visited[j]:
            arr.append(j)
            visited[j] = True
            dfs(curNum+1)
            visited[j] = False
            arr.pop()

# Main
dfs(0)