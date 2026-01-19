def solution(array, commands):
    ret = []
    for c in commands:
        i, j, k = map(int, c)
        
        arr = sorted(array[i-1:j])
        arr.sort()
        ret.append(arr[k-1])
        
    return ret