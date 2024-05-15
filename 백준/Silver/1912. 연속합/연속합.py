"""
1.전략
- DP(Dynamic Programming)
- 각 원소(i)마다 앞의 부분합을 구할 필요 X
- 점화식 : dp[i] = max(arr[i], dp[i-1] + arr[i])

2.시간복잡도
- O(N) = 100,000(Worst case)
  => 1초 이내 가능
"""
import sys; input = sys.stdin.readline

def DP(N: int, arr: list):
    global dp
    
    for i in range(1, N):
        dp[i] = max(arr[i], dp[i-1] + arr[i])

    return max(dp)

# 입력받기
N = int(input())
arr = list(map(int, input().split()))

# 필요한 변수 선언 및 초기화
dp = [min(arr)] * N
dp[0] = arr[0]

# 함수 실행
res = DP(N, arr)

# 결과 출력
print(res)