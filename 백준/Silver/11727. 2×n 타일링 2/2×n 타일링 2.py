"""
1.전략
- 다이나믹 프로그래밍(Dynamic Programming)
- 몇 가지 케이스를 직접 그려보며 다음 그려지는 규칙을 파악
  => 1x2, 2x1 타일은 홀수, 짝수에 모두 그려질 수 있으나 2x2의 타일의 경우 짝수일 때마다 1개씩 더 그릴 수 있음
- 점화식
  - 짝수인 경우: dp[i] = dp[i-1] * 2 + 1
  - 홀수인 경우: dp[i] = dp[i-1] * 2 - 1

2.시간 복잡도
- 시간 제한: 1초
- 시간 복잡도: O(N) = 1,000
"""
import sys
input = sys.stdin.readline

# Input
n = int(input())

# Variables
dp = [0 for _ in range(n+1)]
dp[1] = 1

# Solution
for i in range(2, n+1):
    if i % 2 == 0:
        dp[i] = dp[i-1] * 2 + 1
    else:
        dp[i] = dp[i-1] * 2 - 1

print(dp[n] % 10007)