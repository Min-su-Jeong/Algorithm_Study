import sys

input = sys.stdin.readline
n = int(input())

nums = [i for i in list(map(int, input().split()))]
dp = nums[:]

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+nums[i])
            
print(max(dp))