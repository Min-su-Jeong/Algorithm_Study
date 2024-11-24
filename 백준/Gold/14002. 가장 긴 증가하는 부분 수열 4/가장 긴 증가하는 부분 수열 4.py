"""
1.전략
- 다이나믹 프로그래밍(Dynamic Programming)
- 현재 자릿수(i) 기준으로 증가하는 부분 수열의 최댓값을 누적
- 점화식: A[i] > A[1~i-1]인 경우 => dp[i] = max(dp[i], dp[j]+1)
- 해당하는 부분 수열을 찾기 위해 dp 값이 늘어나는 수만 리스트에 저장

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
dp = [0 for _ in range(N+1)]

# Solution
def DP(n: int):
    global dp

    arr = [[i] for i in A]
    for i in range(1, n+1):
        for j in range(1, i):
            if A[i] > A[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
                arr[i] = arr[j] + [A[i]]

        dp[i] += 1

    return arr

# Output
res = DP(N)
print(max(dp))
print(*res[dp.index(max(dp))])