def solution(s):
    c1, c2 = 0, 0     # 각각의 문자 카운트 변수(c1, c2)
    res = 0           # 결과 변수
    for i in s:       # s의 요소 순차적으로 꺼내기
        if c1 == c2:  # 개수가 같은 경우
            res += 1  # 결과에 +1
            tmp = i   # 해당 단어(x) 임시 저장
        if tmp == i:  # 단어(x)가 i와 같은 글자인 경우
            c1 += 1
        else:         # 단어(x)가 i와 다른 글자인 경우
            c2 += 1

    return res