# 약수의 개수 찾기 함수
def divisor(n):
    dl = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            dl.append(i) 
            if ( (i**2) != n) : 
                dl.append(n // i)
    return len(dl)

def solution(left, right):
    # 범위 내의 수들의 약수 개수를 파악하여 짝수인 경우 +, 홀수인 경우 - 하도록 합산
    return sum([i if divisor(i) % 2 == 0 else -i for i in range(left, right+1)])