import sys
input = sys.stdin.readline

# Input
N = int(input())

# Variables
MAX = 31
dp = [0 for _ in range(MAX)]
dp[2] = 3

# Solution
def solution(n: int):
    global dp

    for i in range(4, n+1, 2):
        dp[i] = dp[i-2]*3 + sum(dp[:i-2])*2 + 2

    return dp[n]

# Main
res = solution(N)

# Output
print(res)