import sys
input = sys.stdin.readline

# Input
A, B = input().split()

# Variables
res = -1
arrA = list(map(int, A.rstrip()))
arrB = list(map(int, B.rstrip()))
length = len(arrA)
visited = [False for _ in range(length)]

# Solution
def dfs(depth: int, curNum: str):
    global res

    if depth == length:
        C = int(curNum)
        if C < int(''.join(map(str, arrB))):
            res = max(res, C)
        return

    for i in range(length):
        if depth == 0 and arrA[i] == 0:
            continue
        
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, curNum+str(arrA[i]))
            visited[i] = False

# Output
dfs(0, '')
print(res)