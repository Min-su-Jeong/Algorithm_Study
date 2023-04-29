def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():   # 대문자인 경우
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A')) # 알파벳 26개, 65번('A')부터 시작
        elif s[i].islower(): # 소문자인 경우
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a')) # 알파벳 26개, 97번('a')부터 시작

    return "".join(s) # 문자를 합쳐 문자열로 변환 후 반환