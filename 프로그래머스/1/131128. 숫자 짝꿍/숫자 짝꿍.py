from collections import Counter

def solution(X, Y):
    ret = ''
    for i in range(9, -1, -1):
        ret += str(i) * min(Counter(X)[str(i)], Counter(Y)[str(i)])
        
    if ret == '':
        return "-1"
    elif ret[0] == '0':
        return "0"
    
    return ret

    