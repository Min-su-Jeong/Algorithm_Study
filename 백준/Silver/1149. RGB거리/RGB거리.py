"""
1.전략
- DP(Dynamic Programming)
- 첫 행을 첫번째 집에 각 색을 칠하는 비용으로 채워넣은 후,
- 이전 집에서 칠한 색을 제외한 색 중 더 저렴한 색을 칠하면 되는 문제

2.시간복잡도
- O(N) = 1,000
  => 0.5초 이내 가능
"""
import sys; input = sys.stdin.readline

def DP(N: int):
  for i in range(1, N):
    # 현재 열을 제외한 i-1행의 열들 중 최솟 값 + 현재 칸 비용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

  return min(dp[N-1])

# 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 필요한 변수 선언 및 초기화
dp = [[0] * 3 for _ in range(N)]
dp[0] = arr[0]

# 함수 실행
res = DP(N)

# 결과 출력
print(res)