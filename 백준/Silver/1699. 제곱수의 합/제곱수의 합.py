import sys
input = sys.stdin.readline

# Input
N = int(input())

# Variables
dp = [i for i in range(N+1)]

# Solution
def DP(n: int):
    global dp

    for i in range(1, n+1):
        for j in range(1, i):
            if i < j*j:
                break

            dp[i] = min(dp[i], dp[i-j*j] + 1)

# Main
DP(N)

# Output
print(dp[N])