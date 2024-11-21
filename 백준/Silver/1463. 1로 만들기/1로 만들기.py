"""
- 다이나믹 프로그래밍(Dynamic Programming)
- N이 2 또는 3으로 나누어 떨어지는 경우와 둘 다 나누어 떨어지지 않아 -1을 하는 경우로 나눌 수 있음
- -1을 먼저 했을 떄의 결과값과 나누어 떨어지는 경우에 나누었을 떄의 결과 값을 비교해서 최솟값 찾기

2.시간 복잡도
- 시간 제한: 0.7초
- O(N) = 10^6 = 1,000,000
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())

# Variables
res = 0
dp = [0 for _ in range(N+1)]

# Solution
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    
# Output
print(dp[N])
