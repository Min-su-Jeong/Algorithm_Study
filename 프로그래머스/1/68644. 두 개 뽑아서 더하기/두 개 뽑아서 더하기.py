def solution(numbers):
    ret = []
    for i in range(len(numbers)):
        for j in range(i):
            ret.append(numbers[i]+numbers[j])
            
    ret = list(set(ret))
    ret.sort()
    
    return ret