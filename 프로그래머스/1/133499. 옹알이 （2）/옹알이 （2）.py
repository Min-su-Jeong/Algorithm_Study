"""
1. babbling 요소 하나씩 꺼내기
2. 문자열에 네 가지 발음 검사
  - 중복인 경우: continue
  - 중복이 아닌 경우: 발음에 해당 하는 글자 공백처리(' ')
- 공백처리 하는 이유: yayae의 경우 - aya 처리 후 ye가 합쳐지게 되어 발음 가능으로 판단 가능  
"""
def solution(babbling):
    ret = 0
    sounds = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for s in sounds:
            if s * 2 in b:
                continue
            
            b = b.replace(s, ' ')
            
        if len(b.strip()) == 0:
            ret += 1
    
    return ret