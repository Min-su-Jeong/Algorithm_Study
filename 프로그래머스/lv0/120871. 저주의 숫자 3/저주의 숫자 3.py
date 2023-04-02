def solution(n):
    res = 0
    # n의 크기만큼 반복
    for i in range(n):
        # 반복횟수만큼 +1
        res += 1
        
        # 3 포함 or 3의 배수인 숫자들의 경우, 한번 더 +1을 해주어야 함.
        while (res % 3 == 0) or ('3' in str(res)):
            res += 1
            
    return res