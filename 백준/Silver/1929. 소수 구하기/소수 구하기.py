m, n = map(int, input().split())

# 소수 판별 함수
def primality(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 입력 받은 범위 내에서 소수 판별
for num in range(m, n+1):
    if primality(num):
        print(num)