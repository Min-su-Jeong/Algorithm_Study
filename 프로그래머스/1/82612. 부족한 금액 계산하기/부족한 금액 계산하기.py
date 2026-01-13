def solution(price, money, count):
    ret = sum([price*(i+1) for i in range(count)])
    ret -= money
    
    if ret < 0:
        return 0
    else:
        return ret