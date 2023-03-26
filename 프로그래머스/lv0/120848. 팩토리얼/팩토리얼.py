import math

def solution(n):
    res = 0
    while(n >= math.factorial(res)):
        res += 1
    return res-1