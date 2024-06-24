"""
1.전략
- DP(Dynamic Programming)
- 1) dp[N-2] 값에 가로 길이 2짜리 타일로 만들수 있는 경우
  -> dp[N-2] * 3
- 2) 0~N-4까지의 타일 뒤에 자신을 붙혀서 만들 수 있는 경우
  -> (dp[0] + dp[2] + ... dp[N-4]) * 2
- 3) 가로 길이가 N인 새로운 타일 덩어리를 만드는 경우
  -> 2
- 3가지 경우의 합을 구함 => dp[N]
- 점화식 : dp[N] = dp[N-2] * 3 + sum(dp[:N-2]) * 2 + 2

2.시간복잡도
- O(N^2) = 30 * 30 = 900 (Worst case)
"""
def DP(N: int):
    global dp

    for i in range(4, N+1):
        if i % 2 == 0:
            dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
        else:
            dp[i] = 0

    return dp[N]

# 입력 받기
N = int(input())

# 필요한 변수 선언 및 초기화
MAX = 31
dp = [0] * MAX
dp[2] = 3

# 함수 실행
res = DP(N)

# 결과 출력
print(res)