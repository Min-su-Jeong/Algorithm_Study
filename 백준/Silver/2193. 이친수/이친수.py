"""
1.전략
- 다이나믹 프로그래밍(Dynamic Programming)
- 두 가지 조건을 생각
  => 0으로 시작할 수 없음
  => N자리 이친수 중, 0으로 끝나는 경우 = +2 / 1로 끝나는 경우 = +1씩 증가함
- 점화식: dp[i] = dp[i-1] + dp[i-2]

2.시간 복잡도
- 시간 제한: 2초
- O(N) = 90
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())

# Variables
dp = [0 for _ in range(N+1)]
dp[1] = 1

# Solution
def DP(n: int):
    global dp

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Main
print(DP(N))