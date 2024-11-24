"""
1.전략
- 다이나믹 프로그래밍(Dynamic Programming)
- 현재 자릿수(i) 기준으로 증가하는 부분 수열의 최댓값을 누적
- 점화식: A[i] > A[1~i-1]인 경우 => dp[i] = max(dp[i], dp[j]+1)

2.시간 복잡도
- 시간 제한: 1초
- O(N^2) = 1,000 * 1,000 = 1,000,000
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())
A = [0] + list(map(int, input().split()))

# Variables
dp = [1 for _ in range(N+1)]

# Solution
def DP(n: int):
    global dp

    for i in range(2, n+1):
        for j in range(1, i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)

# Output
print(DP(N))