"""
1.전략
- 다이나믹 프로그래밍, 수학
- 점화식
  => 제곱수가 현재의 값보다 큰 경우: pass
  => 제곱수가 현재의 값보다 작은 경우: dp[i] = min(dp[i], dp[i-j*j]+ 1)

2.시간 복잡도
- 시간 제한: 2초
- O(N * root(N)) = 100,000 * root(100,000) = 31,622,777
"""
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