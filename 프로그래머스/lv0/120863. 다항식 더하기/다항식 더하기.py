def solution(polynomial):
    res = []
    s1, s2 = 0, 0
    for s in polynomial.split(' + '): # 더하기(' + ') 기준 문자열 나누기
        if s[-1] == 'x': # 일차항(x항)인 경우
            s1 += int(1 if len(s) == 1 else s[:-1]) # 'x'앞에 숫자가 있는 경우, 계수 더하기
                                                    # 'x'앞에 숫자가 없는 경우, 1 더하기
        else: # 상수항인 경우
            s2 += int(s) # 상수 더하기
    
    if s1: # s1 값이 0이 아닌 경우
        res.append('x' if s1 == 1 else '%dx'%(s1))
    if s2: # s2 값이 0이 아닌 경우
        res.append('%d'%(s2))
        
    return ' + '.join(res) # res에 있는 요소들을 ' + ' 로 병합하여 결과 출력