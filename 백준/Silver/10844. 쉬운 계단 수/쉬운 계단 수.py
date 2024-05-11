"""
1.전략
- DP(Dynamic Programming)
- 1~8 뒤에 올 수 있는 숫자는 2종류 / 9는 오직 8만 가능
- 구조 : dp[자릿 수][앞에 오는 숫자] = 경우의 수

  1) 앞에 오는 숫자 = 0
  dp[자릿 수][0] = dp[자릿 수 - 1][1]

  2) 앞에 오는 숫자 = 1~8
     dp[자릿 수][1-8] 
     = dp[자릿 수 - 1][앞에 오는 숫자 -1] + dp[자릿 수 - 1][앞에 오는 숫자 + 1]
 
  3) 앞에 오는 숫자 = 9
     dp[자릿 수][9] = dp[자릿 수 - 1][8]

2.시간복잡도
- O(N) = 100,000
  => 1초 이내 가능
"""
def DP(N: int):
    global dp

    for i in range(2, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
                
    return sum(dp[N]) % MOD

# 입력 받기(테스트 케이스 수)
N = int(input())

# 필요한 변수 선언 및 초기화
MOD = 1000000000
dp = [[0] * 10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

# 함수 실행 및 결과 출력
print(DP(N))