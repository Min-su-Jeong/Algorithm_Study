def solution(nums):
    n = len(nums) // 2
    s = len(set(nums))
    
    if n > s:
        return s
    else:
        return n