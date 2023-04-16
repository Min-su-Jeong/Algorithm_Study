def solution(num):
    for i in range(500): # 500번 반복
        if num == 1:     # num이 1이 되는 경우
            return i     # 반복 횟수 반환
        num = num*3+1 if num % 2 else num/2 # 규칙에 따른 num 결과
    return -1