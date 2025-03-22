import sys
input = sys.stdin.readline

# Input
T = int(input())

# Variables
MAX = 100001
MOD = 1000000009
dp = [[0]*3 for _ in range(MAX)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

# Solution
def solution():
    global dp

    for i in range(4, MAX):
        dp[i][0] = dp[i-1][1] + dp[i-1][2] % MOD
        dp[i][1] = dp[i-2][0] + dp[i-2][2] % MOD
        dp[i][2] = dp[i-3][0] + dp[i-3][1] % MOD

# Main
solution()

for _ in range(T):
    n = int(input())

    res = sum(dp[n]) % MOD
    print(res)