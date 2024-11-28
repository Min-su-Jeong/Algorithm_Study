"""
1.전략
- 다이나믹 프로그래밍(Dynamic Programming)
- 연속 3잔 마시기 불가능 => 케이스 생각 + dp[n]은 n번째까지 최대로 마신 포도주 잔의 개수로 저장
  1. n-2번째까지 최대로 마신 후 n번째 와인 마시기
  2. n-3번째까지 최대로 마신 후 n-1, n번째 와인 마시기
  3. n번째 와인을 안마시는 경우 => n-1번째 값과 최댓값 비교
- 점화식: dp[i] = max(dp[i-1], dp[i-2] + wine[i],  dp[i-3] + wine[i-1] + wine[i])

2.시간 복잡도
- 시간 제한: 2초
- O(N) = 10,000
"""
import sys
input = sys.stdin.readline

# Input
n = int(input())
wine = [0] * 10001
for i in range(1, n+1):
    wine[i] = int(input())

# Variables
dp = [0 for _ in range(10001)]
dp[1] = wine[1]
dp[2] = wine[1] + wine[2]

# Solution
def DP(n: int) -> int:
    global dp

    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i],  dp[i-3] + wine[i-1] + wine[i])

    return max(dp)

# Main
res = DP(n)

# Output
print(res)