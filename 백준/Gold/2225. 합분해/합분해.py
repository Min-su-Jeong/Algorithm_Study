"""
1.전략
- 다이나믹 프로그래밍(Dynamic Programming)
- 2차원 배열을 통해 N, K의 자릿수별로 가질 수 있는 경우의 수 나열
- 점화식: dp[n][k] = dp[n-1][k] + dp[n][k-1]

2.시간 복잡도
- 시간 제한: 2초
- O(N*K) = 200 * 200 = 40,000
"""
import sys
input = sys.stdin.readline

# Input
N, K = map(int, input().split())

# Variables
MOD = 1000000000
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
dp[0][0] = 1

# Solution
def DP():
    global dp

    for i in range(N+1):
        for j in range(1, K+1):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD

# Main
DP()

# Output
print(dp[N][K])