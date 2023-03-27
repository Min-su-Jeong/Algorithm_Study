def solution(i, j, k): 
    # i~j까지의 수를 반복하되 각각의 수를 문자열로 변환
    # 그 후, k가 숫자에 포함되어 있는지 여부를 확인하고 1씩 증가시켜 합을 반환
    return sum(1 for ss in range(i, j+1) for s in str(ss) if k == int(s))