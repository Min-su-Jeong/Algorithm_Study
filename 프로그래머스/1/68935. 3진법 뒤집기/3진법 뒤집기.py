def solution(n):
    num = []
    
    while n > 0:
        num.append(n%3)
        n = n // 3
    
    ret = 0
    for i in range(len(num)):
        ret += num[i] * 3 ** (len(num)-i-1)
        
    return ret