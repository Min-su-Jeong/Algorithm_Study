import sys
input = sys.stdin.readline

# Input
N = int(input())
A = [0] + list(map(int, input().split()))

# Variables
dp = [0 for _ in range(N+1)]

# Solution
def solution(n: int):
    global dp

    for i in range(1, n+1):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j]+A[i])

    return max(dp)

# Main
res = solution(N)

# Output
print(res)