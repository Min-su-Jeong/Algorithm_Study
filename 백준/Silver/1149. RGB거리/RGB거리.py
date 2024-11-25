"""
1.전략
- 다이나믹 프로그래밍(Dynamic Programming)
- 규칙: 이웃 간의 집의 색은 모두 달라야 하며 비용은 최솟값을 가져야 함
- 선택된 행 기준, 같은 열이 아니며 합이 최소가 되는 값을 현재 인덱스에 저장
- 점화식
  => dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
  => dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
  => dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

2.시간 복잡도
- 시간 제한: 0.5초
- O(N) = 1,000
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# Variables
dp = [[1000 for _ in range(3)] for _ in range(N)]
dp[0] = arr[0]

def DP(n: int):
    global dp

    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

    return min(dp[n-1])

# Main
res = DP(N)
print(res)