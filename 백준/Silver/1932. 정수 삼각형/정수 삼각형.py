"""
1.전략
- DP(Dynamic Programming)
- 행의 첫번째 숫자(j = 0)인 경우, 이전 행의 같은 열의 숫자 더하기
- 행의 마지막 숫자(j = i)인 경우, 이전 행의 마지막 열 숫자 더하기
- 이외의 경우, 이전 행의 같은 열(j) 또는 자신의 열 -1인 숫자를 비교해서 큰 값 더하기

2.시간복잡도
- O(N^2) = 500 ^ 2 = 250,000
  => 2초 이내 가능
"""
import sys; input = sys.stdin.readline

def DP(n: int):
  global dp

  for i in range(1, n):
    for j in range(i+1):
      if j == 0:
        dp[i][j] += dp[i-1][0]
      elif j == i:
        dp[i][j] += dp[i-1][j-1]
      else:
        dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

  return max(dp[n-1])

# 입력 받기
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

# 함수 실행
res = DP(n)

# 결과 출력
print(res)