def solution(my_string):
    l = [s.lower() for s in my_string] # 문자열을 문자단위로 분할(소문자로 변환)
    return ''.join(sorted(l))          # 사전순 정렬 후 문자를 문자열로 변환하여 반환