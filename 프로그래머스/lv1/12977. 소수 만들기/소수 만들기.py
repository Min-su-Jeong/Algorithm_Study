from itertools import combinations as cb

# 소수 판별 함수
def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True

def solution(nums):
    # 조합을 사용하여 3개의 수를 뽑고 소수가 되는 경우의 개수를 1씩 증가하여 총 합 반환
    return sum([1 for a,b,c in cb(nums, 3) if isPrime(a+b+c)])
