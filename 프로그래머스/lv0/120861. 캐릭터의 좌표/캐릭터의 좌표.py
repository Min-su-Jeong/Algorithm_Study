def solution(keyinput, board):
    # 가로, 세로 제한 크기
    x_lim, y_lim = board[0]//2, board[1]//2
    
    # 이동 좌표 dict
    move = {"left": (-1,0), "right": (1,0), "up": (0,1),"down": (0,-1)}
    
    # keyinput에 따른 가로, 세로 좌표 이동 
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x, y = x+dx, y+dy

    # 결과 반환
    return [x,y]