def solution(N, stages):
    p = len(stages)
    fail = {}
    for i in range(1, N + 1):
        if p != 0:
            fail[i] = stages.count(i) / p
            p -= stages.count(i)
        else:
            fail[i] = 0

    return sorted(fail, key=lambda i: fail[i], reverse=True)
        