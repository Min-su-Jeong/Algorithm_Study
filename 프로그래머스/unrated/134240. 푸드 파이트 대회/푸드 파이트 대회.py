def solution(food):
    res = []
    for i in range(1, len(food)):
        if food[i] >= 2:
            for j in range(food[i]//2):
                res.append(str(i))
    tmp = list(reversed(res))
    res.append('0')
    
    return ''.join(res + tmp)
            
        