"""
1.전략
- 다이나믹 프로그래밍(Dynamic programming)
- i: 구하고 싶은 카드의 장수
- j: i보다 작은 카드의 장수
- j와 미지수 x의 합이 i가 나와야하기 때문에 
- j + x = i 라는 식을 만족시켜야 함 => x = i - j (i > j)

2.시간복잡도
- O(N^2) = 10,000 * 10,000 = 100,000,000
  => 1초 이내 가능
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())
cost = [0] + list(map(int, input().split()))

# Variables
dp = [0 for _ in range(N+1)]

# Solution
def DP(n) -> int:
    global dp

    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] = max(dp[i], dp[i-j] + cost[j])

    return dp[n]

# Output
print(DP(N))