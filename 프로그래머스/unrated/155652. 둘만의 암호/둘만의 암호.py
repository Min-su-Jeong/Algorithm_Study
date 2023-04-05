def solution(s, skip, index):
    # skip 내의 문자를 제외한 알파벳 리스트 생성
    alpha = [chr(i) for i in range(97, 123) if not chr(i) in skip] * 3 
    
    # s 내의 문자를 가져와 index 뒤의 알파벳으로 변경한 문자를 리스트로 저장 후 join 반환
    return ''.join([alpha[alpha.index(i) + index] for i in s])