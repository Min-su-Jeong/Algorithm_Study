"""
1.전략
- 백트래킹(Back Tracking)
- 중복 X, 사전 순으로 순회하는 DFS 구현
- 가지치기 = 부분 수열의 합이 S와 같아지는 경우 

2.시간 복잡도
- 시간 제한: 2초
- O(2^N) = 2 ^ 20 = 1,048,576
"""
import sys
input = sys.stdin.readline

# Input
N, S = map(int, input().split())
seq = list(map(int, input().split()))

# Variables
res = 0
arr = []

# Solution
def backTracking(curNum:int):
    global res

    if sum(arr) == S and len(arr) > 0:
        res += 1

    for i in range(curNum, N):
        arr.append(seq[i])
        backTracking(i+1)
        arr.pop()

# Main
backTracking(0)

# Output
print(res)