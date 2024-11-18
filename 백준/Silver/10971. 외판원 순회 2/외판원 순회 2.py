"""
1.전략
- 백트래킹(Back Tracking)
- 1 ~ N번까지의 도시를 한번씩 순회하려면 각 행에서 한 번씩만 선택되어야 함.
- 또한, 선택된 행과 열([i,i]) 기준으로 다음 행부터 방문된 열(i)은 갈 수 없음.
- visited: 방문된 열 확인, cost: 누적된 비용 계산, depth: 순회 횟수
- res 값과 비교를 통해 최소 비용 값을 구함

2.시간 복잡도
- 시간 제한: 2초
- O(N!) = 10! = 3,628,800
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# Variables
res = sys.maxsize
visited = [False for _ in range(N)]
visited[0] = True

# Solution
def backTacking(curNum: int, cost: int, depth: int):
    global res

    if depth == N-1 and graph[curNum][0]:
        res = min(res, cost+graph[curNum][0])
        return

    for i in range(N):
        if not visited[i] and graph[curNum][i]:
            visited[i] = True
            backTacking(i, cost+graph[curNum][i], depth+1)
            visited[i] = False

# Main
backTacking(0, 0, 0)

# Output
print(res)