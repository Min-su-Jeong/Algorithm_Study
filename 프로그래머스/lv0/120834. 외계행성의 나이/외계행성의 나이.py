def solution(age):
    return ''.join([chr(int(i)+97) for i in str(age)]) # 나이(age)를 int->str 변경 후 대응하는 아스키코드 값 반환