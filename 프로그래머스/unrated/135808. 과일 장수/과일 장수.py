def solution(k, m, score):
    res = 0 
    score = sorted(score, reverse = True) # 내림차순 정렬(사과 점수)
    
    for i in range(0, len(score), m): # m개씩 건너뛰어 반복
        tmp = score[i:i+m]            # m개 단위로 분할
        if len(tmp) == m:             # 길이가 m이면 
            res += min(tmp) * m       # 현재 m개씩 잘린 사과들 중에 (가장 작은 값 * m) 더하기
            
    return res