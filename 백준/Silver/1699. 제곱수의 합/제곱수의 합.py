"""
1.전략
- DP(Dynamic Programming)
- 최소의 항의 개수 = N보다 작은 가장 큰 제곱수를 구하고 뒤의 항들을 찾기
- 새로운 제곱 수가 등장할 때 1로 초기화되는 규칙 발견
- 점화식 : dp[i] = dp[i - j*j] + 1

2.시간복잡도
- O(N * root(N)) = 100,000 * root(100,000) = 31,622,777
  => 2초 이내 가능
"""
def DP(N: int):
    global dp

    # 경우의 수 구하기
    for i in range(1, N+1):
        for j in range(1, i):

            # i가 제곱 수보다 작은 경우: break
            if i < j*j:
                break
            
            # 점화식
            dp[i] = min(dp[i], dp[i-j*j] + 1)
 
    return dp[N]

# 입력 받기
N = int(input())
dp = [i for i in range(N+1)]

# 함수 실행
res = DP(N)

# 결과 출력
print(res)