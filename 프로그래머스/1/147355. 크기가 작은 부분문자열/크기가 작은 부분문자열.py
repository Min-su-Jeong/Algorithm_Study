"""
- p의 길이 구하기
- p의 길이 만큼 t 부분 문자열 구하기
- 부분 문자열 대수 비교 후 카운트
"""

def solution(t, p):
    ret = 0
    tLen, pLen = len(t), len(p)

    for i in range(tLen-pLen+1):
        if t[i:i+pLen] <= p:
            ret += 1

    return ret