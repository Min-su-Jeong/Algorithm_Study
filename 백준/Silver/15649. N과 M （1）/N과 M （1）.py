"""
1.전략
- Back Tracking
- arr를 만들어 시작할 숫자(i)를 넣은 후 만들 수 있는 조합을 모두 출력
- i가 N일 때까지 반복

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
visited = [False for _ in range(N+2)]
arr = []

# Function
def dfs():
    # 종료 조건
    if len(arr) == M:
        print(*arr)
        return

    # 방문 조건
    for j in range(1, N+1):
        if not visited[j]:
            arr.append(j)
            visited[j] = True
            dfs()
            visited[j] = False
            arr.pop()

# Main
for i in range(1, N+1):
    arr.append(i)
    visited[i] = True
    dfs()
    arr.clear()
    visited[i] = False