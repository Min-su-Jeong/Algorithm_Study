def solution(my_string, n):
    s = [s for s in my_string] # 문자열을 문자단위로 분할
    return ''.join([s[i]*n for i in range(len(s))]) # 배열의 길이만큼 각 문자 n번 반복 후, 문자열로 join하여 반환