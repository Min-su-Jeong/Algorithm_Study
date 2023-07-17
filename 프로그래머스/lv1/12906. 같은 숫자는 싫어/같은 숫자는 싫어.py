def solution(arr):
    result = []
    cur_num = -1
    
    for i in arr:
        if cur_num != i:
            result.append(i)
            cur_num = i
            
    return result