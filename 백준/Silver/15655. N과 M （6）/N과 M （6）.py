"""
1.전략
- 백트래킹(Back Tracking)
- list를 한 개 만들어 관리. DFS + 가지치기 추가
- 중복 x: 방문 여부를 확인 필요
- 수열 오름차순: 입력받은 숫자를 정렬 후 순회 시작
- 시작 값을 기준으로 증가하는 순서여야 하므로 index를 curNum+1을 기준으로 설정

2.시간 복잡도
- 시간 제한: 1초
- O(N^M)
"""
import sys
input = sys.stdin.readline

# Input 
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# Variable
res = []
visited = [False for _ in range(N+1)]

# Solution
def dfs(curNum: int): 
    # 가지치기
    if len(res) == M:
        print(*res)
        return

    # 조건
    for i in range(curNum+1, N+1):
        if not visited[i]:
            res.append(arr[i-1])
            visited[i] = True
            dfs(i)
            res.pop()
            visited[i] = False

# Main
dfs(0)