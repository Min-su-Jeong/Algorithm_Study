def solution(spell, dic):
    # 리스트 -> 집합 자료형으로 변환
    spell = set(spell)
    
    # 사전에서 단어 1개씩 꺼내기
    for d in dic:
        # spell과 사전의 차집합했을 때(두 집합이 완전 일치 시)
        if spell.issubset(set(d)):
            return 1
    return 2