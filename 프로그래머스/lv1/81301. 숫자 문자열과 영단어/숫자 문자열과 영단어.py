def solution(s):
    num_dict = { 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,   # 숫자 사전 생성
                'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9 }
    num_str = '' # 숫자 영단어 저장을 위한 변수
    res = []     # 결과 저장을 위한 변수
    for ss in s: # 문자열을 문자단위로 반복
        if not ss.isdigit():                       # 숫자가 아닌 경우 
            num_str += ss                          # num_str에 문자 추가
            if num_str in num_dict:                # num_str이 숫자 사전에 존재한다면 
                res.append(str(num_dict[num_str])) # res에 추가
                num_str = ''                       # num_str 초기화
        else:                                      # 숫자인 경우
            res.append(str(ss))                    # res에 추가
        
    return int(''.join(res))                       # 리스트를 하나의 문자열로 join 후 int형으로 변환
        