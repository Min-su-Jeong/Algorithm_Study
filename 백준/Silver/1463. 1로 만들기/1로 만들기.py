import sys
input = sys.stdin.readline

# Input
N = int(input())

# Variables
dp = [0 for _ in range(N+1)]

# Solution
def solution():
    global dp

    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
    
# Main
solution()

# Output
print(dp[N])