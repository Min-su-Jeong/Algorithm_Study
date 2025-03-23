import sys
input = sys.stdin.readline

# Input
n = int(input())
arr = [0] + list(map(int, input().split()))

# Variables
dp = [-1000 for _ in range(n+1)]
dp[1] = arr[1]

# Solution
def solution(n: int):
    global dp

    for i in range(1, n+1):
        dp[i] = max(arr[i], dp[i-1]+arr[i])

    return max(dp)

# Main
res = solution(n)

# Output
print(res)