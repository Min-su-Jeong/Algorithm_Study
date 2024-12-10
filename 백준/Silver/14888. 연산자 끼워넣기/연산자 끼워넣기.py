"""
1.전략
- DFS(Depth-First Search)
- 재귀 시에 주어진 각 연산의 개수에 따라 조건문을 나누어 순회하도록 구현
- N만큼 채워지는 경우에 최대,최솟값 비교 연산

2.시간 복잡도
- 시간 제한: 2초
- O(4^N-1) = 4 ^ 10 = 1,048,576
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# Variables
minVal = 10**9
maxVal = -10**9

# Solution
def dfs(i, arr):
    global add, sub, mul, div, maxVal, minVal

    if i == N:
        maxVal = max(maxVal, arr)
        minVal = min(minVal, arr)
        return 
    
    else:
        if add > 0:
            add -= 1
            dfs(i+1, arr + A[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - A[i])
            sub += 1        
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * A[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(arr / A[i]))
            div += 1

# Main
dfs(1, A[0])

# Output
print(maxVal)
print(minVal)