from collections import deque

def bfs(maps, i, j, n, m, visited):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    area = int(maps[i][j])
    
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                visited[nx][ny] = 1
                area += int(maps[nx][ny])
                q.append((nx, ny))
    return area

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    res = []
    
    # bfs 알고리즘을 사용하여 map을 조회하며 방문하지 않은 섬 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                res.append(bfs(maps, i, j, n, m, visited))
    
    return sorted(res) if res else [-1]