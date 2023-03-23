from math import gcd

def solution(numer1, denom1, numer2, denom2):
    # 두 분수의 합 계산(분자, 분모)
    numer = numer1*denom2 + numer2*denom1
    denom = denom1 * denom2
    
    # 최대공약수 구하기
    g = gcd(numer, denom)
    
    # 분자,분모에 대해 최대공약수로 나누어 반환(기약 분수)
    return [numer//g, denom//g]