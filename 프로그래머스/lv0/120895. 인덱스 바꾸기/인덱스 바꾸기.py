def solution(my_string, num1, num2):
    s = [s for s in my_string]          # 문자열->문자로 분할
    s[num1], s[num2] = s[num2], s[num1] # 해당 인덱스의 문자 swap
    return ''.join(s)                   # 문자열로 병합하여 반환