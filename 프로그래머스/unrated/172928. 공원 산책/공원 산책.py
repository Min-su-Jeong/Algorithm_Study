def solution(park, routes):
    dx = {'N':-1 ,'S':1 ,'W':0 ,'E':0 }
    dy = {'N':0 ,'S':0 ,'W':-1 ,'E':1 }
    
    # 시작좌표 찾기(x, y)
    x = -1
    for p in park:
        x += 1
        if 'S' in p:
            y = p.index('S')
            break
            
    # 방향 이동(한 칸씩 이동 -> 조건 만족 시 명령 수행)
    for r in routes:
        op, n = r.split()
        for i in range(1, int(n)+1):
            nx = x + i*dx[op]
            ny = y + i*dy[op]
            # 이동할 수 있다면 현재 방향으로 계속 진행
            if 0 <= nx < len(park) and 0 <= ny < len(park[0]) and park[nx][ny] != 'X':
                continue
            # 이동할 수 없다면 현재 방향 무시
            else:
                break
                
        # 이동 방향 업데이트
        else:
            x, y = nx, ny
        
    return [x, y]