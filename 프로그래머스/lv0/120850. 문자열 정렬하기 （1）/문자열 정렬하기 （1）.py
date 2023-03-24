def solution(my_string):
    return sorted([int(s) for s in my_string if s.isdigit()]) # 문자열->문자로 나누어 숫자 판별 후, 오름차순 정렬하여 반환