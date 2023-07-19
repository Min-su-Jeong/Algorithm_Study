import math
from collections import deque

def solution(progresses, speeds):
    result = []
    
    q = deque()
    for p, s in zip(progresses, speeds):
        q.append(math.ceil((100 - p) / s))

    while q:
        x = q.popleft()
        cnt = 1
        while q:
            y = q.popleft()
            if x >= y:
                cnt += 1
            else:
                q.appendleft(y)
                break
        result.append(cnt)
        
    return result
        
        
        
        