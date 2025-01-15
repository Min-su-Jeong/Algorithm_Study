import sys
input = sys.stdin.readline

# Input
N = int(input())
S = list(map(int, input().split()))
S.sort()

# Variables
res = 0

# Solution
for i in S:
    if res+1 < i:
        break
    res += i

# Output
print(res+1)