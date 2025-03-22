import sys
input = sys.stdin.readline

# Input
N = int(input())
P = list(map(int, input().split()))

# Variables
dp = [0 for _ in range(10001)]

# Solution
def solution(n: int):
    global dp

    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] = max(dp[i], dp[i-j]+P[j-1])

    return dp[n]

# Main
res = solution(N)

# Output
print(res)