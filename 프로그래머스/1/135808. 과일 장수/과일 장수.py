def solution(k, m, score):
    ret = 0
    
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        box = score[i:i+m]
        if len(box) == m:
            ret += min(box) * m
            
    return ret