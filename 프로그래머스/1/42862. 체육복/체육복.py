def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    
    ret = 0
    for i in range(1, n+1):
        if i not in lost:
            ret += 1
        elif i in reserve:
            ret += 1
            reserve.remove(i)
            lost.remove(i)
            
    for i in lost:
        if i-1 in reserve:
            ret += 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            ret += 1
            reserve.remove(i+1)
            
    return ret