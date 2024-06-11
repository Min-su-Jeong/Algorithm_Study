"""
1.전략
- DP(Dynamic Programming)
- i번째 수 기준으로 이전 수들의 증감 여부를 판단
- 증가하는 구간: dp1[i] + 1 / 감소하는 구간: dp2[i] + 1
- dp1과 dp2의 합을 이용해 바이토닉 수열의 조건에 맞는 길이 구하기

2. 시간복잡도
- O(N^2) = 1,000 ^ 2 = 1,000,000 (Worst case)
  => 1초 이내 가능
"""
import sys; input = sys.stdin.readline

def DP(N: int, A: list):
    global dp1, dp2
    
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp1[i] = max(dp1[i], dp1[j]+1)
    
    A.reverse()
    
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp2[i] = max(dp2[i], dp2[j]+1)

    res = [a+b for a, b in zip(dp1, dp2[::-1])]

    return max(res)-1

# 입력 받기
N = int(input())
A = list(map(int, input().split()))

# 필요한 변수 생성 및 초기화
dp1 = [1] * N
dp2 = [1] * N

# 함수 실행
res = DP(N, A)

# 결과 출력
print(res)