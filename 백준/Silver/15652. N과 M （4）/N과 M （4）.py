"""
1.전략
- 백트래킹(Back Tracking)
- list를 한 개 만들어 관리. DFS + 가지치기 추가
- 중복 O: 방문 여부를 확인할 필요 X
- 비내림차순: curNum+1부터 시작하도록 설정 + 중복 허용하도록 다음 재귀 값(i-1)을 설정

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
        arr.append(i)
        dfs(i-1)
        arr.pop()

# Main
dfs(0)