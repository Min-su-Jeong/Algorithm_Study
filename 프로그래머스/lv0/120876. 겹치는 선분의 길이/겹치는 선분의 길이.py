def solution(lines):
    # 각 선분별 집합체 생성
    sets = [set(range(min(l), max(l))) for l in lines]
    
    # 각각의 집합체끼리 & 연산자로 교집합을 구한 후, 겹치는 선분들을 | 연산자로 합집합을 구하여 길이 반환
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    
            