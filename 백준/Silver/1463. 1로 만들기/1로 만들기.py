"""
1.전략
- 다이나믹 프로그래밍(Dynamic programming)
- 상향식(Bottom-up) 접근
- 2와 3으로 나눠지는 경우와 그렇지 않은 경우를 나누어 접근

2.시간복잡도
- O(N) = 10 ^ 6 = 1,000,000 (Worst case)
  => 0.15초 이내 가능
"""
def DP(N: int):
    global dp
    
    for i in range(2, N+1):
        # i에서 1을 빼는 경우
        dp[i] = dp[i-1] + 1
        
        # i가 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
            
        # i가 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
             
    return dp[N]

# 입력 받기
N = int(input())

# 필요한 변수 선언
dp = [0] * (N+1)

# 함수 실행 및 결과 출력
print(DP(N))