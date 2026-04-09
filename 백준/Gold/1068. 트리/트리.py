import sys
input = lambda: sys.stdin.readline().rstrip()

MAX = 51
adj = [[] for _ in range(MAX)]

N = int(input())
arr = list(map(int, input().split()))
rm = int(input())

def dfs(here):
    ret, child = 0, 0
    for there in adj[here]:
        if there == rm: continue
        ret += dfs(there)
        child += 1

    if child == 0: return 1
    return ret

if __name__ == "__main__":
    for i in range(N):
        if arr[i] == -1: root = i
        adj[arr[i]].append(i)

    if root == rm:
        print(0)
    else:
        print(dfs(root))