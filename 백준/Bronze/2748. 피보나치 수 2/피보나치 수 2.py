"""
n의 최댓값: 90

풀이 전략 1
- 피보나치 순환 함수 작성
- n 값을 입력받아 n번쨰 피보나치 수 출력
- 시간 복잡도: O(2^N)

풀이 전략 2 (채택)
- DP 이용
- 시간 복잡도: O(N)
"""

# Input
n = int(input())

# Variables
MAX = 91
dp = [0] * MAX 
dp[1] = 1
dp[2] = 1

# Logic
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

# Output
print(dp[n])