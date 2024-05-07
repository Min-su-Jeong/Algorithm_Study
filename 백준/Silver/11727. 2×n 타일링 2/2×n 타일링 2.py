"""
1.전략
- 다이나믹 프로그래밍(Dynamic programming)
- 1~5까지 몇가지 경우의 수를 구해봄
- 다음과 같은 규칙을 찾게됨
  dp[i] = dp[i-2] * 2 + dp[i-1] (n>2)
- 점화식을 대입하여 dp문제 접근

2.시간복잡도
- O(N) = 1,000
  => 1초 이내 가능
"""
def DP(n: int):
    global dp
    
    for i in range(3, n+1):
        dp[i] = (dp[i-2] * 2 + dp[i-1]) % 10007

    return dp[n]

# 입력 받기
n = int(input())

# 필요한 변수 선언 및 초기화
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

# 함수 실행 및 결과 출력
print(DP(n))