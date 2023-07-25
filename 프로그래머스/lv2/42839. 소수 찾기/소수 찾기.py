from itertools import permutations

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True

def solution(numbers):
    result = []
    
    # numbers에서 나올 수 있는 숫자 리스트 도출
    arr = []
    numbers = [n for n in numbers]
    for i in range(1, len(numbers)+1):
        arr += list(permutations(numbers, i))
    arr = [int(("").join(i)) for i in arr] 
    
    # arr에서 소수인 것만 리스트에 추가 후 중복 제거
    result = len(set([i for i in arr if isPrime(i)]))

    return result
        
        