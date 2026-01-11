from collections import deque

def solution(s):
    ret = 0
    
    q = deque(s)
    while q:
        s1, s2 = 1, 0
        x = q.popleft()
        
        while q:
            y = q.popleft()
            
            if x == y:
                s1 += 1
            else:
                s2 += 1
                
            if s1 == s2:
                ret += 1
                break
                
        if s1 != s2:
            ret += 1
            
    return ret