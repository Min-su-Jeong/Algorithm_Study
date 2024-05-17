"""
1.전략
- DP(Dynamic Programming)
- 숫자 N을 k개로 나타내는 방법 고민
- 귀납적으로 접근(K=1~3)
- 점화식 : dp[K][N] = dp[K-1][N] + dp[K][N-1]

2.시간복잡도
- O(N*K) = 200 * 200 = 40,000(Worst case)
  => 2초 이내 가능
"""
def DP(N: int, K: int):
    global dp

    for i in range(N+1):
        for j in range(1, K+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[N][K] % 1000000000

# 입력 받기
N, K = map(int, input().split())

# 필요한 변수 선언 및 초기화
dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

# 함수 실행
res = DP(N, K)

# 결과 출력
print(res)