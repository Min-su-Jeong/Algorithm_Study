import sys
input = sys.stdin.readline

# Input
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

# Solution
def DP(n: int) -> int:
    global dp

    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

    return max(dp[n-1])

# Main
res = DP(n)

# Output
print(res)