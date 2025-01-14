import sys
input = sys.stdin.readline

# Input
N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

# Variables
res = 0

# Solution
def dfs(index: int, arr: list):
    global res

    if len(arr) >= 2:
        total_sum = sum(arr)
        difficulty_range = max(arr) - min(arr)
        if L <= total_sum <= R and difficulty_range >= X:
            res += 1
    
    for i in range(index, N):
        arr.append(A[i])
        dfs(i + 1, arr)
        arr.pop()

# Main
dfs(0, [])
print(res)