"""
- p의 길이 구하기
- p의 길이 만큼 t 부분 문자열 구하기
- 부분 문자열 대수 비교 후 카운트
"""

def solution(t, p):
    tLen, pLen = len(t), len(p)
    subList = [t[i:i+pLen] for i in range(tLen - pLen + 1)]
    
    ret = 0
    for sub in subList:
        if sub <= p:
            ret += 1

    return ret