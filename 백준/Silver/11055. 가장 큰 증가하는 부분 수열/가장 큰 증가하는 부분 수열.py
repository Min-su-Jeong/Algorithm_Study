"""
1.전략
- DP(Dynamic Programming)
- i번째 수를 기준으로 이전의 수들 중 더 작은 숫자들의 총합을 구함.
- 이를 dp[i]에 누적하여 저장하고 dp 배열 중 가장 큰 값을 구함.
- max(dp) = 부분 수열 중 합이 가장 큰 것

2. 시간복잡도
- O(N^2) = 1,000 ^ 2 = 1,000,000 (Worst case)
  => 1초 이내 가능
"""
def DP(N: int, A: list):
    global dp

    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + A[i])

    return max(dp)

# 입력 받기
N = int(input())
A = list(map(int, input().split()))

# 필요한 변수 생성 및 초기화
dp = A[:]

# 함수 실행
res = DP(N, A)

# 결과 출력
print(res)