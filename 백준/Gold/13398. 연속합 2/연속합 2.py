import sys
input = sys.stdin.readline

# Input
n = int(input())
arr = list(map(int, input().split()))

# Variables
dp = [[-1000 for _ in range(n)] for _ in range(2)]
res = -1000

# Solution
def solution():
    global dp, res

    for i in range(n):
        dp[0][i] = max(arr[i], dp[0][i-1]+arr[i])
        dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])
        res = max(res, dp[0][i], dp[1][i])

    return res

# Main
res = solution()

# Output
print(res)