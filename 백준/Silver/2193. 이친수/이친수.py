"""
1.전략
- DP(Dynamic Programming)
- 규칙을 찾기 위한 1~6까지 경우의 수 계산
- 점화식 : dp[i] = dp[i-1] + dp[i-2] 발견
- 식을 대입하여 dp[n] 값 반환

2.시간복잡도
- O(N) = 90
  => 2초 이내 가능
"""
def DP(N: int):
    global dp
    
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[N]

# 입력 받기
N = int(input())

# 필요한 변수 선언 및 초기화
dp = [0] * (N+1)
dp[1] = 1

# 함수 실행 및 결과 출력
print(DP(N))