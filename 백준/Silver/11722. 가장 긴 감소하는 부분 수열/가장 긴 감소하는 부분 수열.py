"""
1.전략
- DP(Dynamic Programming)
- i번째 수 기준으로 이전 수들의 감소 여부를 판단
- 감소하는 구간이 있는 경우 dp[i]에 1씩 증가
- 점화식 : dp[i] = max(dp[i], dp[j]+1)

2. 시간복잡도
- O(N^2) = 1,000 ^ 2 = 1,000,000 (Worst case)
  => 1초 이내 가능
"""
import sys; input = sys.stdin.readline

def DP(N: int, A: list):
    global dp

    for i in range(1, N):
        for j in range(i):
            if A[i] < A[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)

# 입력 받기
N = int(input())
A = list(map(int, input().split()))

# 필요한 변수 생성 및 초기화
dp = [1] * N

# 함수 실행
res = DP(N, A)

# 결과 출력
print(res)