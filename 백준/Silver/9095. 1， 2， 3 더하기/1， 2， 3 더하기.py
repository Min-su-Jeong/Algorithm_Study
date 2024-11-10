"""
1.전략
- DP(Dynamic Programming)
- 숫자의 조합을 통해 합을 구하는 방식 -> 규칙이 존재할 것 같음
- 1~6까지 경우의 수를 나타내며 규칙 찾아보기
  n=1: 1 / n=2: 2 / n=3: 4 / n=4: 7 / n=5: 13 / n=6: 24
- 규칙을 찾아보며 이전의 값들이 다음 n 값에 영향을 받는다는 것을 알게됨
- 점화식: dp[n] = dp[n-3] + dp[n-2] + dp[n-1]

2.시간 복잡도
- 시간 제한: 1초
- O(N) = 10 * T(Test Case)
"""
import sys
input = sys.stdin.readline

T = int(input())

MAX = 11

dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, MAX):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(T):
    n = int(input())
    print(dp[n])