def solution(board, moves):
    ret = 0
    stk = []
    size = len(board)
    
    for move in moves:
        move -= 1 # 리스트 인덱스 맞추기 위함
        for i in range(size):
            doll = board[i][move]
            
            if doll != 0:
                stk.append(doll)
                board[i][move] = 0
                break
                
        if len(stk) >= 2 and stk[-1] == stk[-2]:
            ret += 2
            stk.pop()
            stk.pop()
        
    return ret