"""
1.전략
- DP(Dynamic Programming)
- dp[0][i]: 수를 제거하지 않고 구하는 연속합
- dp[1][i]: 수를 제거하고 구하는 연속합
- 점화식: dp[1][i] = max(dp[0][i-1], dp[1][i-1] + a[i])

2. 시간복잡도
- O(N) = 100,000(Worst case)
  => 2초 이내 가능
"""
import sys; input = sys.stdin.readline

def DP(n: int, arr: list):
    global dp

    res = -1000
    for i in range(n):
        dp[0][i] = max(arr[i], dp[0][i-1] + arr[i])
        dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])
        res = max(res, dp[0][i], dp[1][i])

    return res

# 입력 받기
n = int(input())
arr = list(map(int,input().split()))

# 필요한 변수 생성 및 초기화
dp = [[-1000]*n for _ in range(2)]

# 함수 실행
res = DP(n, arr)

# 결과 출력
print(res)