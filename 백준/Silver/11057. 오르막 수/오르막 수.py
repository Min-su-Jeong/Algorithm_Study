"""
1.전략
- 다이나믹 프로그래밍(Dynamic Programming)
- i가 증가하면서 0~9까지 각 자릿수별로 1~N까지의 누적합의 경우의 수를 가짐
  ex) 3인 경우: sum(1~10) + sum(1~9) + ... + sum(1)
- 점화식: dp[j] += dp[j-1]

2.시간 복잡도
- 시간 제한: 1초
- O(N^2) = 1,000 * 1,000 = 1,000,000
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())

# Variables
MOD = 10007
dp = [1 for _ in range(10)]

# Solution
def DP(n: int):
    global dp

    for _ in range(n-1):
        for j in range(1, 10):
            dp[j] += dp[j-1]

    return (sum(dp) % MOD)

# Main
res = DP(N)

# Output
print(res)