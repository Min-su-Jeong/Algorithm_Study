"""
1,전략
- DFS
- visited 리스트: 방문 여부 확인
- res 리스트: 순회하면서 N 길이만큼 채워질 때마다 return

2.시간복잡도
- O(N^2): 8 ^ 2 = 64 (Worst case)
  => 1초 이내 가능
"""
def dfs():
    if len(res) == N:
        print(*res)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            res.append(i)
            dfs()
            visited[i] = False
            res.pop()
            
        
N = int(input())
visited = [False] * (N+1)
res = []

dfs()
