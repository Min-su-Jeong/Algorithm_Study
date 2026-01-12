def solution(k, score):
    ret = []
    stk = []
    
    for s in score:
        if len(stk) < k:
            stk.append(s)
        else:
            if s > stk[-1]:
                stk.pop()
                stk.append(s)
        
        stk.sort(reverse=True)
        ret.append(stk[-1])
        
    return ret