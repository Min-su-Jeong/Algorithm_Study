import sys
input = sys.stdin.readline

# Input
N = int(input())
A = [0] + list(map(int, input().split()))

# Variables
dp1 = [0 for _ in range(N+1)]
dp2 = [0 for _ in range(N+1)]

# Solution
def solution(n: int):
    global dp

    for i in range(1, n+1):
        for j in range(i):
            if A[i] > A[j]:
                dp1[i] = max(dp1[i], dp1[j]+1)

    for i in range(n-1, 0, -1):
        for j in range(n, i, -1):
            if A[i] > A[j]:
                dp2[i] = max(dp2[i], dp2[j]+1)

    return max([x + y for x, y in zip(dp1,dp2)])

# Main
res = solution(N)

# Output
print(res)