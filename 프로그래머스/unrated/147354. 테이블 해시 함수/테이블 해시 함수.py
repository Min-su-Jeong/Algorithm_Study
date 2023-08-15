def solution(data, col, row_begin, row_end):
    # 2번 조건
    data.sort(key=lambda x: (x[col-1], -x[0])) 
    
    # 3번 조건
    res = 0
    for idx, row in enumerate(data[row_begin-1:row_end]):
        row_sum = 0
        for r in row:         
            row_sum += r % (idx+row_begin)
        res ^= row_sum
        
    # 4번 조건
    return res
    