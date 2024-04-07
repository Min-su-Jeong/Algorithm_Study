import sys
input = sys.stdin.readline

MAX = 1000001
dp = [0] * MAX # 약수의 합을 저장할 list

for i in range(1, MAX):
    for j in range(i, MAX, i):
        dp[j] += i
    dp[i] += dp[i-1]

for i in range(int(input())):
    n = int(input())
    print(dp[n])