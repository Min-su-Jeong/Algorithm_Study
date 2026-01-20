def isPrime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    ret = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if isPrime(nums[i]+nums[j]+nums[k]):
                    ret += 1
                    
    return ret
            