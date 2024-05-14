"""
1.전략
- DP(Dynamic Programming)
- LIS(Longest Increasing Subsequence) 유형 문제
- 접근 : A[i]를 마지막 값으로 가지는가장 긴 증가 부분수열의 길이 찾기
- 점화식 : dp[i] = max(dp[i], dp[j]+1)
- 해당하는 부분 수열을 찾기 위해 dp 값이 늘어나는 수만 리스트에 저장

2.시간복잡도
- O(N^2) = 1,000 * 1,000 = 1,000,000(Worst case)
  => 1초 이내 가능
"""
import sys; input = sys.stdin.readline

def DP(N: int, A: list):
    global dp
    
    arr = [[x] for x in A]
    curNum = 0
    for i in range(N):
        for j in range(i):
            if A[j] < A[i] and dp[i] < dp[j]:
                dp[i] = dp[j]
                arr[i] = arr[j] + [A[i]]
        
        dp[i] += 1
        
    return arr

# 입력 받기
N = int(input())
A = list(map(int, input().split()))

# 필요한 변수 선언 및 초기화
dp = [0] * (N+1)

# 함수 실행
arr = DP(N, A)

# 결과 출력
res = max(dp)
print(res)
print(*arr[dp.index(res)])