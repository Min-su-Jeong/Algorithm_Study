import sys

input = sys.stdin.readline
n = int(input())
f = [int(input()) for _ in range(n)]
dp = [0]*n

if len(f) <= 2: # 계단이 2개 이하인 경우
    print(sum(f))
else: # 계단이 3개 이상인 경우
    dp[0] = f[0]
    dp[1] = f[0] + f[1]
    for i in range(2, n): # 점화식 이용
        dp[i] = max(dp[i-3] + f[i-1] + f[i], dp[i-2] + f[i])
    print(dp[-1])