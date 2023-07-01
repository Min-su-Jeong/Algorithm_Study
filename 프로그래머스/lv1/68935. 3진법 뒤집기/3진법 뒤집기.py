def solution(n):
    res = []
    
    # n(10진법) -> n(3진법)
    while n > 0:
        res.append(n%3)
        n //= 3
    res = res[::-1]
    
    # n(3진법) -> (10진법)
    return sum([res[i] * 3 ** i for i in range(len(res))])
        