"""
1.전략
- 다이나믹 프로그래밍(Dynamic Programming)
- 이전의 값들이 다음 값에 어떻게 반영되는지 규칙 찾기
- 점화식: dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

2.시간 복잡도
- 시간 제한: 1초
- O(N) = 1,000,000
"""
import sys
input = sys.stdin.readline

# Input
T = int(input())

# Variables
MAX = 1000001
MOD = 1000000009
dp = [0 for _ in range(MAX)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

# Solution
def DP():
    global dp

    for i in range(4, MAX):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD 

# Main
DP()

for _ in range(T):
    # Input
    N = int(input())

    # Output
    res = dp[N] % MOD
    print(res)