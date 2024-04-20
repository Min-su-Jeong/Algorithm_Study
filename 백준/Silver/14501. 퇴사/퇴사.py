"""
1.전략
- DP(Dynamic Programming)
- Case 1. i일 상담 X : dp[i+1] 
  => 지난 상담까지의 이익
- Case 2. i일 상담 O : dp[t[i]+i] + p[i] 
  => dp[i일 + i일에 시작할 상담에 필요한 일 수] + 이익
  
2. 시간복잡도
- 완전탐색의 경우 : O(2^N) = 2^15 = 32,768
- DP의 경우 : O(N) = 15
  => 2초 이내 가능
"""
import sys; input = sys.stdin.readline

N = int(input())
counsel = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in reversed(range(N)):
    # i일 상담 기간이 최사일을 초과하는 경우 상담 X
    if i + counsel[i][0] > N:
        dp[i] = dp[i+1]
    else:
        # i일에 상담 하는 것과 안하는 것 중 큰 것 선택
        dp[i] = max(dp[i+1], counsel[i][1] + dp[i + counsel[i][0]])
        
print(dp[0])