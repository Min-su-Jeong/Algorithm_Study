def solution(s):
    ret = False
    stk = []
    
    for ss in s:
        if len(stk) == 0:
            if ss == ")":
                return False
            stk.append(ss)
            
        else:
            if stk[-1] == "(":
                if ss == ")":
                    stk.pop()
                else:
                    stk.append(ss)
        
    if stk:
        return False
    else:
        return True