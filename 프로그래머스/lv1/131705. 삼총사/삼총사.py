from itertools import combinations as cb

def solution(number):
    # 학생 3명의 정수 조합 중 합이 0인 경우 1씩 증가하여 합을 반환
    return sum(1 for c in list(cb(number, 3)) if sum(c) == 0)
