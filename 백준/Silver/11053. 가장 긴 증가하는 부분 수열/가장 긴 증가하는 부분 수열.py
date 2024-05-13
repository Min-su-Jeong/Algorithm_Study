"""
1.전략
- DP(Dynamic Programming)
- LIS(Longest Increasing Subsequence) 유형 문제
- 접근 : A[i]를 마지막 값으로 가지는가장 긴 증가 부분수열의 길이 찾기
- 점화식 : dp[i] = max(dp[i], dp[j]+1)

2.시간복잡도
- O(N^2) = 1,000 * 1,000 = 1,000,000(Worst case)
  => 1초 이내 가능
"""
def solution(A: list, N: int):
    global dp

    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)

# 입력받기
N = int(input())
A = list(map(int, input().split()))

# 필요한 변수 선언 및 초기화
dp = [1] * N

# 함수 실행
res = solution(A, N)

# 결과 출력
print(res)