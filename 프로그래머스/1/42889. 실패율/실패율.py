def solution(N, stages):
    fail = {}
    
    a, b = 0, len(stages)
    for stage in range(1, N+1):
        if b != 0:
            a = stages.count(stage)
            fail[stage] = a / b
            b -= a
        else:
            fail[stage] = 0
            
    ret = sorted(fail, key=lambda x: fail[x], reverse=True)
    return ret