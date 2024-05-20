"""
1.전략
- DP(Dynamic Programming)
- 연속 사용 가능
- n을 나타내는 방법중에 마지막 숫자가 각각 1,2,3으로 끝나는 경우의 수를 생각
- 1~5까지 귀납적으로 접근. 다음과 같은 규칙을 발견함
- 점화식 : dp[n] = dp[n-3] + dp[n-2] + dp[n-1]

2.시간복잡도
- O(N) = 1,000,000
  => 1초 이내 가능
"""
def DP():
    global dp, MAX, MOD

    for i in range(4, MAX):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

# 입력 받기(테스트 케이스 수)
T = int(input())

# 필요한 변수 선언 및 초기화
MOD = 1000000009
MAX = 1000001
dp = [0] * MAX
dp[1], dp[2], dp[3] = 1, 2, 4

# 함수 실행
DP()

for i in range(T):
    # 입력 받기 (n)
    n = int(input())
    
    # 결과 계산 및 출력
    res = dp[n] % MOD
    print(res)