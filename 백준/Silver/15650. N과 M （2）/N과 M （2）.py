"""
1.전략
- 백트래킹

2.시간복잡도
O(N^2) = 8 * 8 = 64
=> 1초 내 가능
"""
def backTracking(curNum):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if not visited[i] and curNum < i:
            visited[i] = True
            arr.append(i)
            backTracking(i)
            visited[i] = False
            arr.pop()
        
N, M = map(int, input().split())
arr = []
visited = [False] * (N+1)

backTracking(0)