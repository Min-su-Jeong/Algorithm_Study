"""
1.전략
- DP(Dynamic Programming)
- 두 사자는 옆 또는 위 아래에 겹치게 위치할 수 없음
- 2x1 우리를 하나씩 추가할 때마다, 새로운 사자를 놓는 경우와 반대의 경우 생각
- 점화식: dp[i] = dp[i-1] + 2*(dp[i-2] + (dp[i-1]-dp[i-2])/2) = 2*dp[i-1]+dp[i-2]
  
2.시간복잡도
- O(N) = 100,000
  => 2초 이내 가능
"""
def DP(N: int):
    global dp, MOD

    for i in range(3, N+1):
        dp[i] = (2 * dp[i-1] + dp[i-2]) % MOD

    return dp[N]

# 입력 받기(테스트 케이스 수)
N = int(input())

# 필요한 변수 선언 및 초기화
MOD = 9901
MAX = 100001
dp = [0] * MAX
dp[1], dp[2] = 3, 7

# 함수 실행
res = DP(N)

# 결과 출력
print(res)