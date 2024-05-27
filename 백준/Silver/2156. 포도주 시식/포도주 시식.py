"""
1.전략
- DP(Dynamic Programming)
- n-2까지의 최대 양 + 현재 양 = (dp[n-2] + wine[n])
- n-3까지의 최대 양 + 전(n-1)번째 양 + 현재 양 = (dp[n-3] + wine[n-1] + wine[n])

2.시간복잡도
- O(N) = 10,000
  => 2초 이내 가능
"""
import sys; input = sys.stdin.readline

def DP(n: int):
  global dp, wine

  # 1. 현재 포도주를 마시지 않았을 경우
  # 2. 현재 포도주와 이전 포도주를 마셨을 경우
  # 3. 마시지 않았을 경우를 비교
  for i in range(3, n+1): 
    dp[i] = max(dp[i - 1], wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2])

  return max(dp)

# 입력 받기
n = int(input())
wine = [0] * 10001
for i in range(1, n+1):
    wine[i] = int(input())

# 필요한 변수 선언 및 초기화
dp = [0] * 10001
dp[1] = wine[1]
dp[2] = wine[1] + wine[2]

# 함수 실행
res = DP(n)

# 결과 출력
print(res)