from math import gcd
def solution(n):
    return ((6*n) // gcd(6, n)) // 6 # 6과 n의 최소공배수에서 6으로 나눈 몫 반환