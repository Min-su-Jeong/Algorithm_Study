import sys
input = sys.stdin.readline

# Input
N = int(input())
W = list(map(int, input().split()))

# Variables
res = 0

# Solution
def dfs(curSum: int):
    global res

    if len(W) == 2:
        res = max(res, curSum)
        return res
    
    for i in range(1, len(W)-1):
        curNum = W.pop(i)
        dfs(curSum + W[i-1] * W[i])
        W.insert(i, curNum)
        
# Main
dfs(0)

# Output
print(res)