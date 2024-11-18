"""
1.전략
- 백트래킹(Back Tracking)
- 1) 주어진 식을 계산하는 함수 구현
- 2) 주어진 배열에 대해 나올 수 있는순서를 계산하기 위해 dfs 사용
- res 값과 비교하여 최댓값 계산

2.시간 복잡도
- 시간 제한: 1초
- O(N*N!) = 8 * 8! = 322,560
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())
A = list(map(int, input().split()))

# Variables
res = -sys.maxsize
visited = [False for _ in range(N+1)]
arr = []

# Function 1. 식 계산
def calcSum(arr: list):
    s = 0
    for i in range(1, len(arr)):
        s += abs(arr[i-1] - arr[i])
    
    return s

# Function 2. 순회하며 최댓값 구하기
def backTracking(curNum: int):
    global res

    if curNum == N:
        res = max(res, calcSum(arr))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(A[i])
            backTracking(curNum+1)
            visited[i] = False
            arr.pop()

# Main
backTracking(0)

# Output
print(res)