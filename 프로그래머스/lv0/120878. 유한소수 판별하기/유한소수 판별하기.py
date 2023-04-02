from math import gcd

def solution(a, b):
    # 최대공약수로 나누기(기약분수 만들기)
    b //= gcd(a,b)
    
    # 소인수분해(2와 5)
    while b%2 == 0:
        b //= 2
    while b%5 == 0:
        b //= 5
        
    # 최종적으로 b가 1이된 경우, 유한소수로 판별 
    return 1 if b == 1 else 2