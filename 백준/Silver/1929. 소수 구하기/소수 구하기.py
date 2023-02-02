m, n = map(int, input().split())

# 소수 판별 함수
def primality(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# 입력 받은 범위 내에서 소수 판별
for num in range(m, n+1):
    if primality(num):
        print(num)
    else:
        continue