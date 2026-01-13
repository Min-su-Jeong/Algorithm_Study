"""
1. babbling 요소 하나씩 꺼내기
2. 문자열에 네 가지 발음 중에 포함되는지 여부 확인
  - 존재하면: flag 값 업데이트(중복 여부 판단), 인덱스 해당 길이만큼 더해서 스킵
  - 존재하지 않으면: 발음 불가 -> flag 값으로 판단하기
"""
def solution(babbling):
    ret = 0
    
    for b in babbling:
        """
1. babbling 요소 하나씩 꺼내기
2. 문자열에 네 가지 발음 중에 포함되는지 여부 확인
  - 존재하면: flag 값 업데이트(중복 여부 판단), 인덱스 해당 길이만큼 더해서 스킵
  - 존재하지 않으면: 발음 불가 -> flag 값으로 판단하기
"""
def solution(babbling):
    ret = 0
    sounds = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for s in sounds:
            if s * 2 in b:
                continue
            
            b = b.replace(s, " ")
            
        if len(b.strip()) == 0:
            ret += 1
            
    return ret
                