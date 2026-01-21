def solution(arr):
    ret = []
    ret.append(arr[0])
    
    for i in range(1, len(arr)):
        if ret[-1] == arr[i]:
            continue
        
        ret.append(arr[i])
        
    return ret
        