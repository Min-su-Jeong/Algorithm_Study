"""
1.전략
- 다이나믹 프로그래밍(Dynamic Programming)
- 크게 3가지의 규칙이 있음
  => 1. 0: 0을 제외한 나머지는 시작 숫자로 지정 가능
  => 2. 1~8: 뒤에 올 수 있는 숫자가 총 2종류
  => 3. 9: 뒤에 8만 올 수 있음
- 점화식
  => 0인 경우: dp[i][0] = dp[i-1][1]
  => 1~8인 경우: dp[i][Num] = dp[i-1][Num-1] + dp[i-1][Num+1]
  => 9인 경우: dp[i][9] = dp[i-1][8]

2.시간 복잡도
- 시간 제한: 1초
- O(N)
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())

# Variables
dp = [[0 for _ in range(10)] for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1
    
# Solution
def DP(n: int):
    global dp

    for i in range(2, n+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    return sum(dp[N]) % 1000000000

# Output
print(DP(N))