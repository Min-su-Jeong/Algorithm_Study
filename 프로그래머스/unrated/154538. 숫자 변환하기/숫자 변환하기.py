def solution(x, y, n):
    res = 0
    s = set()
    s.add(x)
    while s:
        # s에 y가 존재하는 경우 
        if y in s:
            return res
        
        # 3가지 경우에 대해 계산
        nxt = set()
        for i in s:
            if i+n <= y:
                nxt.add(i+n)
            if i*2 <= y:
                nxt.add(i*2)
            if i*3 <= y:
                nxt.add(i*3)
        s = nxt
        res += 1

    return -1