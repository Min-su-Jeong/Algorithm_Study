from collections import deque
                        
def solution(board):
    # 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
    dx = [1, -1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, 1, 1, -1, -1]
    
    # 보드 크기
    length = len(board)
    
    # 방문여부를 확인하기 위한 리스트
    visited = [[False] * length for _ in range(length)]

    # bfs 사용
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        while q:
            a, b = q.popleft()   # 왼쪽부터 좌표 꺼내기
            visited[a][b] = True # 방문 시, True로 변경
            for i in range(8):   # 8방향 탐색 
                nx = dx[i] + a
                ny = dy[i] + b

                # 위험지역, 안전지역 탐색 
                if 0<= nx < length and 0<= ny < length and not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        q.append((nx, ny)) # 안전지역
                    else:
                        board[nx][ny] = -1 # 위험지역
                    
    # bfs 탐색
    [bfs(i, j) for i in range(length) for j in range(length) if board[i][j] == 1]
    
    # 안전지역 칸 수 세기
    res = sum([board[i].count(0) for i in range(length)])
    
    return res