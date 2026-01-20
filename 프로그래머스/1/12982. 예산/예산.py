def solution(d, budget):
    ret = 0
    
    d.sort()
    for cost in d:
        budget -= cost
        if budget >= 0:
            ret += 1
        else:
            break
    
    return ret