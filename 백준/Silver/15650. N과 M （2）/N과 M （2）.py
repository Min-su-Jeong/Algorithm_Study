"""
1.전략
- 백트래킹(Back Tracking)
- list를 한 개 만들어 관리. DFS + 가지치기 추가
- 순열 내에 숫자가 중복될 수 없도록 구현
- 오름차순: 시작하는 수(curNum)부터 시작하도록 함

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
    if len(arr) == M:
        print(*arr)
        return

    # 방문 조건
    for i in range(curNum+1, N+1):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            dfs(i)
            arr.pop()
            visited[i] = False

# Main
dfs(0)