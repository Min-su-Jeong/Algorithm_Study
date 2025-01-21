import sys
input = sys.stdin.readline

# Input
S1 = list(input().rstrip())
S2 = list(input().rstrip())

# Variables
lcs = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]

# Solution
for i in range(1, len(S1)+1):
    for j in range(1, len(S2)+1):
        if S1[i-1] == S2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

# Output
print(lcs[-1][-1])