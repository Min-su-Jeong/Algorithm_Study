def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

T = int(input())

while T:
    N = int(input())
    
    if isPrime(1 + N):
        print(1)
        print(1, 1 + N)
    else:
        print(0)
        
    T -= 1