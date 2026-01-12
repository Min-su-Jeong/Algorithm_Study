def solution(a, b, n):
    ret = 0
    
    while a <= n:
        ret += (n // a) * b
        n = (n // a) * b + (n % a)
        
    return ret