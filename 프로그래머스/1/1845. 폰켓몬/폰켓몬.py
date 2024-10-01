def solution(nums):
    # 중복을 제외한 폰켓몬 수와 가질 수 있는 수의 최솟 값 비교
    num1 = len(set(nums))
    num2 = len(nums) // 2
    
    return min(num1, num2)