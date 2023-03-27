def solution(my_string):
    # 숫자 판별 후 아닌 경우에만 공백(' ') 처리 => 숫자만 남기기
    my_string = "".join([s if s.isdigit() else ' ' for s in list(my_string)])
    return sum(int(s) for s in my_string.split()) # 리스트에 남겨진 숫자 모두 더하여 반환