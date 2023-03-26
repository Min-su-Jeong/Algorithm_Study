def solution(my_string):
    return ''.join(list(dict.fromkeys(my_string))) # dict.fromkeys를 이용한 중복제거, 리스트 변환 후 문자 병합하여 반환