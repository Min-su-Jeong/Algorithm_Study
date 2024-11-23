"""
1.전략
- DP(Dynamic Programming)
- 세 가지의 숫자 연속 사용 불가 => n행 3열짜리 리스트 필요
  dp[n][0] = n을 나타내는 방법중에 마지막 숫자가 1로 끝나는 경우의 수를 저장
  dp[n][1] = n을 나타내는 방법중에 마지막 숫자가 2로 끝나는 경우의 수를 저장
  dp[n][2] = n을 나타내는 방법중에 마지막 숫자가 3으로 끝나는 경우의 수를 저장

  dp[n][0] = n보다 1작은 수인 n-1의 dp값중에 2와 3으로 끝나는 경우의 합을 저장
  dp[n][1] = n보다 2작은 수인 n-2의 dp값중에 1과 3으로 끝나는 경우의 합을 저장
  dp[n][2] = n보다 3작은 수인 n-3의 dp값중에 1과 2로 끝나는 경우의 합을 저장

2.시간복잡도
- O(N) = 100,000
  => 1초 이내 가능
"""
import sys
input = sys.stdin.readline

# Input
T = int(input())

# Variables
MAX = 100001
MOD = 1000000009
dp = [[0 for _ in range(3)] for _ in range(MAX)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

# Solution
for i in range(4, MAX):
    dp[i][0] = dp[i-1][1] + dp[i-1][2] % MOD
    dp[i][1] = dp[i-2][0] + dp[i-2][2] % MOD
    dp[i][2] = dp[i-3][0] + dp[i-3][1] % MOD

# Main
for i in range(T):
    # Input
    n = int(input())

    # Output
    res = sum(dp[n]) % MOD
    print(res)