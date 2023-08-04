n = int(input())

# 소수 판별 함수
def isPrime(x):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if x % i == 0:
            return False
    return True

while True:
    if str(n) == str(n)[::-1]: # 팰린드롬 수 판별
        if isPrime(n):         # 소수 판별
            print(n)
            break
    n += 1