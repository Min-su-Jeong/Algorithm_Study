n = int(input())
num = list(map(int, input().split()))
cnt = 0

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

for i in num:
    if primality(i):
        cnt += 1
        
print(cnt)