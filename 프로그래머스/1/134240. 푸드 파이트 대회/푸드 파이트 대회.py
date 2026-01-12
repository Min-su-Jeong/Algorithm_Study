def solution(food):
    ret = "0"
    
    for i in range(len(food)-1, 0, -1):
        c = food[i] // 2
        while c > 0:
            ret = str(i) + ret + str(i)
            c -= 1
            
    return ret
    
    