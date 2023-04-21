def solution(n):
    # 문자열로 변환 후 내림차순으로 정렬
    lst = sorted([s for s in str(n)], reverse=True)
    
    # join 하여 한 문자열로 합친 후 int형으로 변환
    return int(''.join(lst))
        