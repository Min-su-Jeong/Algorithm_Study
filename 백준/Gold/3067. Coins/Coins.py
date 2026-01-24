"""
풀이 전략
- 동전 조합 (중복 허용, 순서 무관)
- DP 사용
- dp[x]를 x원을 만드는 경우의 수로 생각
- 각 동전을 한 번씩만 기준으로 사용
- 현재 동전으로 만들 수 있는 금액을 누적 갱신
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [0] * (target+1)
    dp[0] = 1

    for coin in coins:
        for money in range(coin, target+1):
            dp[money] += dp[money-coin]

    print(dp[target])