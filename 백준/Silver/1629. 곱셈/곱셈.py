import sys
a, b, c = map(int, sys.stdin.readline().split())

# 분할정복(모듈러 연산)
def power(a, b, c):
    if b == 1:
        return a%c
    tmp = power(a, b//2, c)
    if b%2 == 0: # b가 짝수
        return tmp*tmp % c
    else: # b가 홀수
        return tmp*tmp*a % c
    
print(power(a, b, c))