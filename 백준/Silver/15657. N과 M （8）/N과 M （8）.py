"""
1.전략
- 백트래킹(Back Tracking)
- list를 한 개 만들어 관리. DFS + 가지치기 추가
- 중복 O: 방문 여부를 확인 필요 X
- 비내림차순: 시작 숫자와 같거나 커야함

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

# Solution
def dfs(curNum: int): 
    # 가지치기
    if len(res) == M:
        print(*res)
        return

    # 조건
    for i in range(curNum, N):
        res.append(arr[i])
        dfs(i)
        res.pop()

# Main
dfs(0)